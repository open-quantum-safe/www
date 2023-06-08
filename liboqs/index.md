---
layout: default
title: liboqs
nav_order: 3
has_children: true
has_toc: false
---

# liboqs

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/liboqs">liboqs on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

liboqs is an open source C library for quantum-safe cryptographic algorithms.

liboqs provides:


- a collection of open-source implementations of quantum-safe key encapsulation mechanism (KEM) and digital signature algorithms (see the [list of supported algorithms](algorithms))
- a common API for these algorithms
- a test harness and benchmarking routines

## Overview

**Open source**. liboqs is a C library for quantum-safe cryptographic algorithms, released under the MIT License. liboqs incorporates some external components which use a different license.

**Multi-platform**. liboqs builds on Linux, macOS, and Windows, supports x86_64 and ARM architectures (except Windows on ARM64), and the clang, gcc, and Microsoft compilers.  Toolchains are available for cross-compiling to other platforms.

**Common API**. liboqs uses a common API for post-quantum key encapsulation and signature algorithms, making it easy to switch between algorithms. Our API closely follows the NIST/SUPERCOP API, with some additional wrappers and data structures.

**Testing and benchmarking**. liboqs includes a test harness and benchmarking routines to compare performance of post-quantum implementations in a common framework.

**Application integrations**. We provide integrations of liboqs into forks of a range of cryptographic [applications and protocols](../applications).

**Language wrappers**. Post-quantum algorithms from liboqs can be used in a variety of other programming languages using the provided [wrappers](wrappers).

Post-quantum algorithm implementations in liboqs are derived from the reference and optimized code submitted by teams to the NIST Post-Quantum Cryptography Standardization Project.  Some implementations come directly from teams; others come via the [PQClean project](https://github.com/PQClean/PQClean).  See the [algorithm datasheets](algorithms) for the lineage of each algorithm's implementation.

## Releases

- [version 0.8.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.8.0) (June 7, 2023) <span class="label label-green">current version</span>
- [version 0.7.2](https://github.com/open-quantum-safe/liboqs/releases/tag/0.7.2) (August 21, 2022)
- [version 0.7.1](https://github.com/open-quantum-safe/liboqs/releases/tag/0.7.1) (December 16, 2021)
- [version 0.7.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.7.0) (August 11, 2021)
- [version 0.6.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.6.0) (June 8, 2021)
- [version 0.5.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.5.0) (March 10, 2021)
- [version 0.4.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.4.0) (August 11, 2020)
- [version 0.3.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.3.0) (June 10, 2020)
- [version 0.2.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.2.0) (October 8, 2019)
- [version 0.1.0](https://github.com/open-quantum-safe/liboqs/releases/tag/master-0.1.0) (November 13, 2018)
- [all releases](https://github.com/open-quantum-safe/liboqs/releases)
