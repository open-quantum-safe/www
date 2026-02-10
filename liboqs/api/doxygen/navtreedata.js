/*
 @licstart  The following is the entire license notice for the JavaScript code in this file.

 The MIT License (MIT)

 Copyright (C) 1997-2020 by Dimitri van Heesch

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software
 and associated documentation files (the "Software"), to deal in the Software without restriction,
 including without limitation the rights to use, copy, modify, merge, publish, distribute,
 sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or
 substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 @licend  The above is the entire license notice for the JavaScript code in this file
*/
var NAVTREE =
[
  [ "liboqs", "index.html", [
    [ "Overview", "index.html#overview", null ],
    [ "Status", "index.html#status", [
      [ "Supported Algorithms", "index.html#supported-algorithms", [
        [ "Key encapsulation mechanisms", "index.html#key-encapsulation-mechanisms", null ],
        [ "Signature schemes", "index.html#signature-schemes", null ],
        [ "Stateful signature schemes", "index.html#stateful-signature-schemes", null ]
      ] ],
      [ "Limitations and Security", "index.html#limitations-and-security", [
        [ "Platform limitations", "index.html#platform-limitations", null ],
        [ "Support limitations", "index.html#support-limitations", null ]
      ] ]
    ] ],
    [ "Quickstart", "index.html#quickstart", [
      [ "Linux and Mac", "index.html#linux-and-mac", null ],
      [ "Windows", "index.html#windows", null ],
      [ "Cross compilation", "index.html#cross-compilation", null ]
    ] ],
    [ "Documentation", "index.html#documentation", null ],
    [ "Contributing", "index.html#contributing", null ],
    [ "License", "index.html#license", null ],
    [ "Acknowledgements", "index.html#acknowledgements", null ],
    [ "Options for configuring liboqs builds", "options-for-configuring-liboqs-builds.html", [
      [ "BUILD_SHARED_LIBS", "options-for-configuring-liboqs-builds.html#bUILD_SHARED_LIBS", null ],
      [ "CMAKE_BUILD_TYPE", "options-for-configuring-liboqs-builds.html#cMAKE_BUILD_TYPE", null ],
      [ "CMAKE_INSTALL_PREFIX", "options-for-configuring-liboqs-builds.html#cMAKE_INSTALL_PREFIX", null ],
      [ "OQS_ENABLE_KEM_ALG/OQS_ENABLE_SIG_ALG/OQS_ENABLE_SIG_STFL_ALG", "options-for-configuring-liboqs-builds.html#oQS_ENABLE_KEM_ALGOQS_ENABLE_SIG_ALGOQS_ENABLE_SIG_STFL_ALG", null ],
      [ "OQS_ALGS_ENABLED", "options-for-configuring-liboqs-builds.html#oQS_ALGS_ENABLED", null ],
      [ "OQS_BUILD_ONLY_LIB", "options-for-configuring-liboqs-builds.html#oQS_BUILD_ONLY_LIB", null ],
      [ "OQS_MINIMAL_BUILD", "options-for-configuring-liboqs-builds.html#oQS_MINIMAL_BUILD", null ],
      [ "OQS_DIST_BUILD", "options-for-configuring-liboqs-builds.html#oQS_DIST_BUILD", null ],
      [ "OQS_USE_CPUFEATURE_INSTRUCTIONS", "options-for-configuring-liboqs-builds.html#oQS_USE_CPUFEATURE_INSTRUCTIONS", null ],
      [ "OQS_USE_OPENSSL", "options-for-configuring-liboqs-builds.html#oQS_USE_OPENSSL", [
        [ "OQS_DLOPEN_OPENSSL", "options-for-configuring-liboqs-builds.html#oQS_DLOPEN_OPENSSL", null ],
        [ "OQS_USE_CUPQC", "options-for-configuring-liboqs-builds.html#oQS_USE_CUPQC", null ],
        [ "OQS_USE_ICICLE", "options-for-configuring-liboqs-builds.html#oQS_USE_ICICLE", null ]
      ] ],
      [ "Stateful Hash Based Signatures", "options-for-configuring-liboqs-builds.html#stateful-hash-based-signatures", null ],
      [ "OQS_OPT_TARGET", "options-for-configuring-liboqs-builds.html#oQS_OPT_TARGET", null ],
      [ "OQS_SPEED_USE_ARM_PMU", "options-for-configuring-liboqs-builds.html#oQS_SPEED_USE_ARM_PMU", null ],
      [ "USE_COVERAGE", "options-for-configuring-liboqs-builds.html#uSE_COVERAGE", null ],
      [ "USE_SANITIZER", "options-for-configuring-liboqs-builds.html#uSE_SANITIZER", null ],
      [ "OQS_ENABLE_TEST_CONSTANT_TIME", "options-for-configuring-liboqs-builds.html#oQS_ENABLE_TEST_CONSTANT_TIME", null ],
      [ "OQS_STRICT_WARNINGS", "options-for-configuring-liboqs-builds.html#oQS_STRICT_WARNINGS", null ],
      [ "OQS_EMBEDDED_BUILD", "options-for-configuring-liboqs-builds.html#oQS_EMBEDDED_BUILD", null ],
      [ "OQS_LIBJADE_BUILD", "options-for-configuring-liboqs-builds.html#oQS_LIBJADE_BUILD", null ],
      [ "OQS_ENABLE_LIBJADE_KEM_ALG/OQS_ENABLE_LIBJADE_SIG_ALG", "options-for-configuring-liboqs-builds.html#oQS_ENABLE_LIBJADE_KEM_ALGOQS_ENABLE_LIBJADE_SIG_ALG", null ],
      [ "OQS_BUILD_FUZZ_TESTS", "options-for-configuring-liboqs-builds.html#oQS_BUILD_FUZZ_TESTS", null ]
    ] ],
    [ "Security Policy", "security-policy.html", [
      [ "Supported Versions", "security-policy.html#supported-versions", null ],
      [ "Reporting a Vulnerability", "security-policy.html#reporting-a-vulnerability", null ],
      [ "Threat Model", "security-policy.html#threat-model", null ],
      [ "Security Response Process", "security-policy.html#security-response-process", null ]
    ] ],
    [ "Data Structures", "annotated.html", [
      [ "Data Structures", "annotated.html", "annotated_dup" ],
      [ "Data Structure Index", "classes.html", null ],
      [ "Data Fields", "functions.html", [
        [ "All", "functions.html", null ],
        [ "Variables", "functions_vars.html", null ]
      ] ]
    ] ],
    [ "Files", "files.html", [
      [ "File List", "files.html", "files_dup" ],
      [ "Globals", "globals.html", [
        [ "All", "globals.html", "globals_dup" ],
        [ "Functions", "globals_func.html", null ],
        [ "Typedefs", "globals_type.html", null ],
        [ "Enumerations", "globals_enum.html", null ],
        [ "Enumerator", "globals_eval.html", null ],
        [ "Macros", "globals_defs.html", "globals_defs" ]
      ] ]
    ] ]
  ] ]
];

var NAVTREEINDEX =
[
"aes__ops_8h.html",
"sig_8h.html#a57207e06fb4c8c1401104f3b6f1cd066",
"struct_o_q_s___a_e_s__callbacks.html#a7d5d60f6bc62119363e68568160a9b2f"
];

var SYNCONMSG = 'click to disable panel synchronization';
var SYNCOFFMSG = 'click to enable panel synchronization';
var LISTOFALLMEMBERS = 'List of all members';