---
layout: default
title: Post-quantum cryptography
nav_order: 1
has_children: false
has_toc: false
---

# Post-quantum cryptography

Public key cryptography is essential in securing all Internet communications. For example, the Transport Layer Security (TLS) protocol uses public key cryptography to protect every "https" web page for entering passwords or credit card numbers. However, all public key algorithms used in practice are based on mathematical problems—such as factoring, discrete logarithms, or elliptic curves—which could be broken by a quantum computer.

The field of quantum-safe cryptography, also called post-quantum or quantum-resistant cryptography, aims to construct public key cryptosystems that are believed to be secure even against quantum computers. Ongoing advancements in physics point toward the eventual construction of large-scale quantum computers. Such future devices would still be able to decrypt present-day communications, allowing anyone to decrypt data transmitted today. Thus, it is important to start developing and deploying quantum-safe cryptography now, even before quantum computers are built.

Several mathematical techniques have been proposed for constructing quantum-safe cryptosystems, including:

- hash functions and symmetric zero-knowledge proofs
- error correcting codes
- lattices (including the learning with errors (LWE) and NTRU problems)
- multivariate equations
- supersingular elliptic curve isogenies

Post-quantum cryptography is an active area of research.  The [PQCrypto conference series](https://pqcrypto.org/conferences.html) has since 2006 been the main academic research conference series devoted to post-quantum cryptography.  Many papers on post-quantum cryptography are published in other academic journals and conferences.  The book [Post-Quantum Cryptography](https://www.springer.com/gp/book/9783540887010) edited by Bernstein, Buchmann, and Dahmen gives an overview of the field as of 2009, but the field has advanced considerably in recent years.

The worldwide effort for developing and standardizing is centred around the [NIST Post-Quantum Cryptography Standardization Project](https://csrc.nist.gov/projects/post-quantum-cryptography).  Starting in 2016, the NIST PQC project issued a call for proposals for quantum-resistant digital signature and key encapsulation mechanisms, kicking off a multi-year project to standardize one or more quantum-resistant cryptosystems after several rounds of public review and comment.  The projected timeline for the project sees draft standards available between 2022--2024.
