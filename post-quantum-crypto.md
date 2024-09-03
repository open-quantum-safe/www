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

## Standardization of post-quantum cryptography

The worldwide effort for developing and standardizing is centred around the [NIST Post-Quantum Cryptography Standardization Project](https://csrc.nist.gov/projects/post-quantum-cryptography).  In 2016, the NIST PQC project issued a call for proposals for quantum-resistant digital signature and key encapsulation mechanisms, kicking off a multi-year project to standardize one or more quantum-resistant cryptosystems after several rounds of public review and comment. In 2022, NIST announced its selection of 4 algorithms for standardization: the key encapsulation mechanism CRYSTALS-Kyber, and three signature schemes CRYSTALS-Dilithium, Falcon, and SPHINCS+. In 2023, NIST released draft standards for 3 of those algorithms. In 2024, NIST published FIPS 202, 203, and 204, specifying the ML-KEM (Kyber), ML-DSA (Dilithium), and SLH-DSA (SPHINCS+) algorithms. NIST continues to evaluate additional post-quantum algorithms for potential standardization.

Standardization of post-quantum algorithms is also taking place in other bodies.  The [Crypto Forum Research Group](https://datatracker.ietf.org/rg/cfrg/about/) within the Internet Engineering Task Force has standardized two stateful hash-based signature schemes (XMSS and LMS/HSS).  The International Organization for Standardization (ISO) is also considering the standardization of several post-quantum algorithms.
