---
layout: default
title: About our project
nav_order: 2
has_children: true
has_toc: false
---

# About the Open Quantum Safe project

The goal of the Open Quantum Safe (OQS) project is to support the development and prototyping of quantum-resistant cryptography.

OQS consists of two main lines of work: [liboqs](liboqs), an open source C library for quantum-resistant cryptographic algorithms, and prototype [integrations](applications) into protocols and applications, including a fork of the widely used OpenSSL library.

OQS is intended for prototyping and evaluating quantum-resistant cryptography. Security of proposed quantum-resistant algorithms may rapidly change as research advances, and may ultimately be completely insecure against either classical or quantum computers.

We believe that the NIST Post-Quantum Cryptography standardization project is currently the best avenue to identifying potentially quantum-resistant algorithms. OQS does not intend to "pick winners", and we strongly recommend that applications and protocols rely on the outcomes of the NIST standardization project when deploying post-quantum cryptography.

While there are many other advanced cryptographic primitives that need to be updated to have quantum resistance, our focus is currently on post-quantum KEMs and signature schemes in the NIST PQC standardization project.

## Limitations

While at the time of this writing there are no vulnerabilities known in any of the quantum-safe algorithms used in the OQS project, it is advisable to wait on deploying quantum-safe algorithms until further guidance is provided by the standards community, especially from the NIST standardization project.  

We realize some parties may want to deploy quantum-safe cryptography prior to the conclusion of the NIST standardization project.  We strongly recommend such attempts make use of so-called **hybrid cryptography**, in which quantum-safe public-key algorithms are used alongside traditional public key algorithms (like RSA or elliptic curves) so that the solution is at least no less secure than existing traditional cryptography.

**WE DO NOT CURRENTLY RECOMMEND RELYING ON LIBOQS OR OUR APPLICATION INTEGRATIONS IN A PRODUCTION ENVIRONMENT OR TO PROTECT ANY SENSITIVE DATA.** This project is meant to help with research and prototyping.  While we make a best-effort approach to avoid security bugs, software in our project has not received the level of auditing and analysis that would be necessary to rely on it for high security use.

For information about bug reporting, please see our [security policy](security).

## Getting started

The easiest way to get started with experimenting with post-quantum cryptography is to use our pre-built Docker images containing post-quantum-enabled versions of OpenSSL/curl, Apache httpd, and nginx. See the [applications and protocols](applications) section for more information.

For developers, there is also a [developer image](https://hub.docker.com/r/openquantumsafe/curl-dev) ready to support incremental development and code installations.

## Research

See a list of [research papers and outcomes based on the OQS project](research).

## Citing OQS

If you make use of liboqs and would like to cite it in an academic paper, we suggest the following:

<blockquote>
    Douglas Stebila, Michele Mosca. Post-quantum key exchange for the Internet and the Open Quantum Safe project. In Roberto Avanzi, Howard Heys, editors, <i>Selected Areas in Cryptography (SAC) 2016</i>, <i>LNCS</i>, vol. 10532, pp. 1–24. Springer, October 2017. <a href="https://openquantumsafe.org">https://openquantumsafe.org</a>
</blockquote>