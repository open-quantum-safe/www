---
layout: default
title: About our project
nav_order: 3
has_children: true
has_toc: false
---

# About the Open Quantum Safe project
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The goal of the Open Quantum Safe (OQS) project is to support the transition to quantum-resistant cryptography.

OQS consists of two main lines of work: [liboqs](liboqs), an open source C library for quantum-resistant cryptographic algorithms, and prototype [integrations](applications) into protocols and applications, including a fork of the widely used OpenSSL library.

OQS began as a research project to enable the prototyping and evaluation of quantum-resistant cryptography. As the field of post-quantum cryptography starts to mature with emerging standards, the OQS project continues to further improve our existing codebase and strengthen our code quality checks on implementations of standards-track algorithms that are intended to be used in deployments.  In parallel, we also plan to maintain an experimental-track version of our suite to support ongoing research and development in new post-quantum cryptography algorithms and evolving PQ capabilities.

Early adopters of post-quantum cryptography should proceed with caution.  We believe that open standardization processes such as the NIST Post-Quantum Cryptography standardization project are the best avenue to identifying potentially quantum-resistant algorithms. OQS does not intend to "pick winners", and we strongly recommend that applications and protocols rely on the outcomes of the NIST standardization project when deploying post-quantum cryptography.  Security of proposed quantum-resistant algorithms may rapidly change as research advances, and may ultimately be completely insecure against either classical or quantum computers, and adopters may want to carefully consider the hybrid use of post-quantum and traditional algorithms to manage risk.

While there are many other advanced cryptographic primitives that need to be updated to have quantum resistance, our focus is currently on post-quantum KEMs and signature schemes in the NIST PQC standardization project.

## Limitations

While at the time of this writing there are no vulnerabilities known in any of the quantum-safe algorithms used in the OQS project, it is advisable to wait on deploying quantum-safe algorithms until further guidance is provided by the standards community, especially from the NIST standardization project.  

We realize some parties may want to deploy quantum-safe cryptography prior to the conclusion of the NIST standardization project.  We strongly recommend such attempts make use of so-called **hybrid cryptography**, in which quantum-safe public-key algorithms are used alongside traditional public key algorithms (like RSA or elliptic curves) so that the solution is at least no less secure than existing traditional cryptography.

**WE DO NOT CURRENTLY RECOMMEND RELYING ON LIBOQS OR OUR APPLICATION INTEGRATIONS IN A PRODUCTION ENVIRONMENT OR TO PROTECT ANY SENSITIVE DATA.** This project is meant to help with research and prototyping.  While we make a best-effort approach to avoid security bugs, software in our project has not received the level of auditing and analysis that would be necessary to rely on it for high security use.

liboqs is not as full-featured as a general purpose encryption library. Among its limitations, it presents cryptographic primitives in the exact form as used in the NIST standardization project: as signature schemes and key encapsulation mechanisms (KEMs).  liboqs does not provide an interface for public key encryption, although such a primitive can be build from KEMs.

### Security policy

For information about bug reporting, please see our [security policy](../liboqs/security).

## Getting started

The easiest way to get started with experimenting with post-quantum cryptography is to use our pre-built Docker images containing post-quantum-enabled versions of OpenSSL/curl, Apache httpd, and nginx. See the [applications and protocols](../applications) section for more information.

For developers, there is also a [developer image](https://hub.docker.com/r/openquantumsafe/curl-dev) ready to support incremental development and code installations.

## Research

See a list of [research papers and outcomes based on the OQS project](../research).

## Citing OQS

If you make use of liboqs and would like to cite it in an academic paper, we suggest the following:

<blockquote>
    Douglas Stebila, Michele Mosca. Post-quantum key exchange for the Internet and the Open Quantum Safe project. In Roberto Avanzi, Howard Heys, editors, <i>Selected Areas in Cryptography (SAC) 2016</i>, <i>LNCS</i>, vol. 10532, pp. 1–24. Springer, October 2017. <a href="https://openquantumsafe.org">https://openquantumsafe.org</a>
</blockquote>