import jinja2
from lxml import etree
import os
import sys

def render_text_and_children(element):
  global env
  s = ''
  if element.text: s += element.text
  for child in element:
    if child.tag == 'ndash': s += '–'
    elif child.tag == 'ref': s += child.text
    elif child.tag == 'computeroutput': s += env.get_template('base/computeroutput').render(t = child.text)
    elif child.tag == 'para': s += env.get_template('base/para').render(t = render_text_and_children(child))
    elif child.tag == 'verbatim': s += env.get_template('base/verbatim').render(t = render_text_and_children(child))
    if child.tail: s += child.tail
  return s

def render_text_and_children_or_empty(element, path):
    a = element.xpath(path)
    if len(a) > 0: return render_text_and_children(a[0])
    return ''

def element_text_or_empty(element, path):
    a = element.xpath(path)
    if len(a) > 0: return a[0].text
    return ''

def attribute_or_empty(element, path):
    a = element.xpath(path)
    if len(a) > 0: return a[0]
    return ''

def object_or_empty(element, path):
    a = element.xpath(path)
    if len(a) > 0: return a[0]
    return ''

class DXFunctionDescriptionParam(object):
  def __init__(self, element, function):
    self.element = element
    self.function = function
  def name(self):
    return render_text_and_children_or_empty(self.element, 'parameternamelist/parametername')
  def description(self):
    return render_text_and_children_or_empty(self.element, 'parameterdescription')
  def type(self):
    for p in self.function.args():
      if self.name() == p.declname(): return p.type()
    return ''

class DXFunctionParam(object):
  def __init__(self, element):
    self.element = element
  def type(self):
    return render_text_and_children_or_empty(self.element, 'type')
  def declname(self):
    return render_text_and_children_or_empty(self.element, 'declname')
  def defname(self):
    return render_text_and_children_or_empty(self.element, 'defname')
  def tostring(self):
    return (self.type() + ' ' + self.declname() + ' ' + self.defname()).strip()

class DXMember(object):
  def name(self):
    return element_text_or_empty(self.element, 'name')
  def uniqid(self):
    return attribute_or_empty(self.element, '@id')
  def src_filename(self):
    return attribute_or_empty(self.element, 'location/@file')
  def src_linenumber(self):
    return attribute_or_empty(self.element, 'location/@line')
  def type(self):
    return render_text_and_children_or_empty(self.element, 'type')
  def definition(self):
    return render_text_and_children_or_empty(self.element, 'definition')
  def args(self):
    return [DXFunctionParam(p) for p in self.element.xpath('param')]
  def argsstring(self):
    return render_text_and_children_or_empty(self.element, 'argsstring')
  def description_brief(self):
    return render_text_and_children_or_empty(self.element, 'briefdescription')
  def description_detailed(self):
    return render_text_and_children_or_empty(self.element, 'detaileddescription')
  def description_parameter_list(self):
    a = self.element.xpath('detaileddescription//parameterlist')
    if len(a) == 0: return []
    else: return [DXFunctionDescriptionParam(p, self) for p in a[0]]
  def return_description(self):
    return render_text_and_children_or_empty(self.element, 'detaileddescription//simplesect[@kind="return"]')
  def initializer(self):
    return render_text_and_children_or_empty(self.element, 'initializer')

class DXDefine(DXMember):
  def __init__(self, element):
    self.element = element

class DXEnumValue(DXMember):
  def __init__(self, element):
    self.element = element

class DXEnum(DXMember):
  def __init__(self, element):
    self.element = element
  def values(self):
    return [DXEnumValue(v) for v in self.element.xpath('enumvalue')]

class DXFunction(DXMember):
  def __init__(self, element):
    self.element = element

class DXIncludes(object):
  def __init__(self, element):
    self.element = element
  def local(self):
    a = attribute_or_empty(self.element, '@local')
    return not(a == '' or a == 'no')
  def filename(self):
    return self.element.text

class DXTypedef(DXMember):
  def __init__(self, element):
    self.element = element

class DXVariable(DXMember):
  def __init__(self, element):
    self.element = element
  def definition(self):
    return render_text_and_children_or_empty(self.element, 'definition')

class DXCompound(object):
  @staticmethod
  def factory(element):
    kind = attribute_or_empty(element, 'compounddef/@kind')
    if kind == 'file': return DXFile(element)
    elif kind == 'struct': return DXStruct(element)
    raise TypeError('Unknown kind: ' + kind)
  def name(self):
    return element_text_or_empty(self.element, 'compounddef/compoundname')
  def path(self):
    a = attribute_or_empty(self.element, 'compounddef/location/@file')
    if len(a) > 0:
      if len(os.path.dirname(a)) > 0: return os.path.dirname(a) + '/'
    return ''
  def src_filename(self):
    return attribute_or_empty(self.element, 'location/@file')
  def description_brief(self):
    return render_text_and_children_or_empty(self.element, 'compounddef/briefdescription')
  def description_detailed(self):
    return render_text_and_children_or_empty(self.element, 'compounddef/detaileddescription')
  def includes(self):
    return [DXIncludes(f) for f in self.element.xpath('compounddef/includes')]

class DXFile(DXCompound):
  def __init__(self, element):
    self.element = element
  def defines(self):
    return [DXDefine(f) for f in self.element.xpath('//memberdef[@kind="define"]')]
  def enums(self):
    return [DXEnum(f) for f in self.element.xpath('//memberdef[@kind="enum"]')]
  def functions(self):
    return [DXFunction(f) for f in self.element.xpath('//memberdef[@kind="function"]')]
  def typedefs(self):
    return [DXTypedef(f) for f in self.element.xpath('//memberdef[@kind="typedef"]')]

class DXStruct(DXCompound):
  def __init__(self, element):
    self.element = element
  def src_linenumber(self):
    return attribute_or_empty(self.element, 'location/@line')
  def variables(self):
    return [DXVariable(f) for f in self.element.xpath('//memberdef[@kind="variable"]')]

def render(templatefilename, xmlfilename, srcbaseurl=''):
  global env
  env = jinja2.Environment(
    loader = jinja2.FileSystemLoader('templates')
  )
  template = env.get_template(templatefilename)
  tree = etree.parse(xmlfilename)
  return template.render(file = DXCompound.factory(tree), srcbaseurl=srcbaseurl)

if __name__ == "__main__":
  if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python3 jinja_doxygen_xml.py template xmlfile [srcbaseurl]")
    exit(1)
  
  templatefilename = sys.argv[1]
  xmlfilename = sys.argv[2]
  srcbaseurl = '' if len(sys.argv) < 4 else sys.argv[3]
  print(render(templatefilename, xmlfilename, srcbaseurl))
