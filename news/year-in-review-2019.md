---
layout: default
title: Year in review – 2019
nav_order: 2
has_children: false
has_toc: true
parent: About our project
---
# Year in review – 2019

*January, 2020*

## Software releases

Our major software goal for the year was updating our core library, liboqs, and our associated sub-projects, to use algorithms from Round 2 of the NIST Post-Quantum Crypto standardization project.  

Algorithms advancing to Round 2 were announced in January 2019, with revisions due in March 2019.  Shortly thereafter we began integrating revised versions into liboqs.  Part of this procedure included reorganizing how we structured liboqs: we deprecated the old "nist-branch", and consolidated all Round 2 algorithms onto liboqs master branch.  We also substantially improved our testing infrastructure, expanding our use of continuous integration systems to test all commits on a larger range of platforms.

In October 2019, we made a coordinated release of liboqs and our associated sub-projects.  

**liboqs version 0.2.0** included support for KEMs from 7 families (BIKE, FrodoKEM, Kyber, NewHope, NTRU, Saber, and SIDH/SIKE), and 5 families of signatures (Dilithium, MQDSS, Picnic, qTesla, and SPHINCS+).

Our October 2019 snapshot releases of **OQS-OpenSSL-1.0.2** and **OQS-OpenSSL-1.1.1** provided post-quantum algorithms in TLS.  The 1.0.2 branch provided basic support for post-quantum and hybrid key exchange in TLS 1.2.  The 1.1.1 provided support for post-quantum and hybrid key exchange and authentication in TLS 1.3.  At the same time we also released a snapshot of **OQS-OpenSSH** with post-quantum and hybrid key exchange and authentication in SSH version 2.

New for 2019 were our **language-specific SDKs** which provide interfaces to post-quantum algorithms in various languages.  We currently provide wrappers in **C++**, **Go**, **.NET**, and **Python**.

In 2019 we also enlarged the ecosystem of **application software** that can rely on OQS tools.  We now curate instructions and Docker images for building and running post-quantum-enabled OpenSSL-reliant applications such as the Apache httpd and nginx web servers, and the command-line web client curl.  We have started on enabling post-quantum algorithms in a fork of BoringSSL and Chromium.

## Papers and Presentations

In 2019, members of the OQS team released two academic papers based on the framework.  The first, published at the NIST 2nd Post-Quantum Cryptography Standardization Conference in August 2019, reported on the feasibility and compatibility of various post-quantum key exchange and authentication methods in TLS and SSH (https://eprint.iacr.org/2019/858).  The second, released as an eprint in December 2019, reports on the performance of post-quantum algorithms in TLS under various network conditions (https://eprint.iacr.org/2019/1447).

We gave presentations at international conferences and events throughout the year, including:

- DefCon Crypto Village
- Dell/VMWare PQC Forum
- ETSI-IQC Workshop 
- IBM Research Zurich
- IETF Montreal meeting 105
- NIST 2nd Post-Quantum Cryptography Standardization Conference
- NorthSec 2019
- Shmoocon 2019
- University of Grenoble-Alpes

## Impact

Anecdotally, our impact has grown substantially this year.  Many people at conferences seem to be familiar with OQS, and it seems to come up frequently in panels and presentations.

Our Github repositories have more than 675 "stars" and our core library liboqs has been forked 125 times.  

In May 2019 Utimaco and evolutionQ issued a press release about a demonstration of post-quantum crypto in hardware security modules relying on OQS software (https://hsm.utimaco.com/news/utimaco-evolutionq-set-standards-by-taking-post-quantum-crypto-open-source/).

In November 2019 some new papers came out from non-OQS authors that relied on the OQS suite, including one on VPNs (https://eprint.iacr.org/2019/1277) and another on signatures (https://eprint.iacr.org/2019/1276).

## Partners

We continue to receive great participation and support from **Amazon Web Services**, **evolutionQ**, and **Microsoft Research**, who have been essential to the success of the project.

In 2019 we were pleased to welcome some new partners:

- **IBM Research Zurich** has started participating in OQS, starting with adding post-quantum support to the S/MIME / CMS tools in OpenSSL, and helping with Docker images and toolchains for development.
- **Cisco Systems** started contributing to OQS as well, leading to a research paper on PQ signatures (https://eprint.iacr.org/2019/1276).
- Our friends at Radboud University in the Netherlands started a new open-source software project in 2019, **PQClean**, which collects together standalone C implementations of post-quantum algorithms.  We use some of the implementations from PQClean in liboqs.

Financial support for OQS in 2019 came from Amazon Web Services and the Tutte Institute for Mathematics and Computing.  Research projects based on OQS were supported by funding from the Natural Sciences and Engineering Research Council of Canada (NSERC).  Microsoft Research donated computation time on Azure.

## Plans for 2020

Over the next few weeks, we will engage in a round of consultation with our partners and participants to set goals for 2020, then release our annual plan.

Thanks to all who have helped OQS advance over the past year! 
 
*Douglas Stebila*<br />
*Project leader, Open Quantum Safe project*
