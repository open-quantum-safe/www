import jinja2
from lxml import etree
import os
import sys

def textAndChildren(node):
  if node.text:
    yield node.text
  for child in node:
    yield child
    if child.tail:
      yield child.tail
      
def a_function_desc_parameterlist(f):
  if len(f.xpath('detaileddescription//parameterlist')) == 0:
    return []
  else: 
    return [p for p in f.xpath('detaileddescription//parameterlist')[0]]

def foldername(p):
  if len(os.path.dirname(p)) > 0:
    return os.path.dirname(p) + '/'
  else:
    return ''

def render(templatefilename, xmlfilename, srcbaseurl=''):
  tree = etree.parse(xmlfilename)
  env = jinja2.Environment(
    loader = jinja2.FileSystemLoader('templates')
  )
  template = env.get_template(templatefilename)
  template.globals['textAndChildren'] = textAndChildren
  template.globals['a_function_desc_parameterlist'] = a_function_desc_parameterlist
  template.globals['xml_to_string'] = etree.tostring
  template.globals['foldername'] = foldername
  doc = dict()
  doc['base'] = tree
  doc['defines'] = tree.xpath('//memberdef[@kind="define"]')
  doc['functions'] = tree.xpath('//memberdef[@kind="function"]')
  return template.render(doc=doc, srcbaseurl=srcbaseurl)

if __name__ == "__main__":
  if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python3 jinja_doxygen_xml.py template xmlfile [srcbaseurl]")
    exit(1)
  
  templatefilename = sys.argv[1]
  xmlfilename = sys.argv[2]
  srcbaseurl = '' if len(sys.argv) < 4 else sys.argv[3]
  print(render(templatefilename, xmlfilename, srcbaseurl))
