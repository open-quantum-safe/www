---
layout: default
title: FAQ
nav_order: 2
has_children: false
has_toc: false
---

# Frequently Asked Questions

### What is post-quantum?  What does quantum-safe mean?

PQ stands for **post-quantum cryptography**, which is cryptography that aims to be resistant to attack by quantum computers.  Post-quantum cryptography is also sometimes called **quantum-resistant cryptography** or **quantum-safe cryptography**.  See our [short primer on post-quantum cryptography](/post-quantum-crypto) or read more details at [Wikipedia](https://en.wikipedia.org/wiki/Post-quantum_cryptography).

### Does post-quantum cryptography require a quantum computer?

No, post-quantum cryptography does not require a quantum computer to run: post-quantum algorithms can be implemented on today's computers.  Post-quantum means that the algorithms are conjectured to be secure even if an attacker someday has a quantum computer.

### Are post-quantum algorithms really secure?

Like most cryptography algorithms, post-quantum cryptography algorithms rely on assumptions that certain mathematical problems are hard to break.  In general, we do not have proofs that these mathematical problems are in fact hard to break, but mathematicians and cryptographers around the world who have studied these algorithms intently have not been able to succeed in breaking them.  

### What is the status of PQ standardization?

The worldwide effort for developing and standardizing is centred around the [NIST Post-Quantum Cryptography Standardization Project](https://csrc.nist.gov/projects/post-quantum-cryptography).  In 2016, the NIST PQC project issued a call for proposals for quantum-resistant digital signature and key encapsulation mechanisms, kicking off a multi-year project to standardize one or more quantum-resistant cryptosystems after several rounds of public review and comment. In 2022, NIST announced its selection of 4 algorithms for standardization: the key encapsulation mechanism CRYSTALS-Kyber, and three signature schemes CRYSTALS-Dilithium, Falcon, and SPHINCS+. In 2023, NIST released draft standards for 3 of those algorithms, with a goal of publishing those standards in 2024.  NIST continues to evaluate additional post-quantum algorithms for potential standardization.

Standardization of post-quantum algorithms is also taking place in other bodies.  The [Crypto Forum Research Group](https://datatracker.ietf.org/rg/cfrg/about/) within the Internet Engineering Task Force has standardized two stateful hash-based signature schemes (XMSS and LMS/HSS).  The International Organization for Standardization (ISO) is also considering the standardization of several post-quantum algorithms.

As of February 2024, here is the status of the standards-track post-quantum algorithms:

Key encapsulation mechanisms:

- ML-KEM a.k.a. CRYSTALS-Kyber: [draft standard from NIST](https://csrc.nist.gov/pubs/fips/203/ipd)

Digital signature schemes:

- ML-DSA a.k.a. CRYSTALS-Dilithium: [draft standard from NIST](https://csrc.nist.gov/pubs/fips/204/ipd)
- Falcon: draft standard under development by NIST
- SLH-DSA a.k.a. SPHINCS+: [draft standard from NIST](https://csrc.nist.gov/pubs/fips/205/ipd)
- XMSS: [standard from CFRG / IRTF](https://www.rfc-editor.org/rfc/rfc8391.html)
- LMS/HSS: [standard from CFRG / IRTF](https://www.rfc-editor.org/rfc/rfc8554.html)

### What's a key encapsulation mechanism?

A [**key encapsulation mechanism (KEM)**](https://en.wikipedia.org/wiki/Key_encapsulation_mechanism) is a public key cryptographic scheme that allows two parties to establish a shared secret key using only public communication. The primary security property provided  by a KEM is confidentiality.  

KEMs are closely related to [public key encryption](https://en.wikipedia.org/wiki/Public-key_cryptography), with one major difference: in a public key encryption scheme, the sender can choose a message to transmit confidentially to the receiver, whereas in a KEM, the sender cannot choose the message to be sent, instead the shared secret key that is established by the KEM between the sender and the receiver is random, not controlled by either the sender or the receiver.  KEMs can be viewed as a generalization of [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).

KEMs are often used in secure channel establishment protocols like TLS in order to set up a symmetric encryption key that is subsequently used in a symmetric key encryption scheme like AES to encrypt application data.

### How can I sign things using a Kyber certificate?

Kyber is a key encapsulation mechanism (see the above question to learn more about KEMs), not a digital signature scheme.  This means that the security goal of Kyber is confidentiality, not authentication.  You need to use a digital signature scheme like ML-DSA (Dilithium) in order to digitally sign a message.

### What is OQS?

The Open Quantum Safe project is an open-source software project to support the development and prototyping of post-quantum cryptography.  Read more about the OQS project on our [about](/about) page.

### Is OQS safe to use?

Read about the limitations of our software on our [about](/about) page.

### How can I use post-quantum cryptography in TLS / X.509 / S/MIME/CMS?

The easiest way to get started in experimenting with post-quantum algorithms in network protocols like TLS, X.509, and S/MIME or CMS is to use OpenSSL 3 combined with the [oqs-provider](https://github.com/open-quantum-safe/oqs-provider), which adds support for all the post-quantum algorithms supported by the OQS project into those network protocols in OpenSSL 3-reliant applications.

You can also get started with our pre-built Docker images for experiments in many applications in our [OQS Demos repository](https://github.com/open-quantum-safe/oqs-demos/).

### How can I use post-quantum cryptography in &lt;my favourite programming language&gt;?

Our [liboqs](https://github.com/open-quantum-safe/liboqs/) project is a C language library with support for many post-quantum algorithms.  We have thin wrappers that provide bindings for these algorithms in many languages, including [C++](https://github.com/open-quantum-safe/liboqs-cpp/), [Go](https://github.com/open-quantum-safe/liboqs-go), [Java](https://github.com/open-quantum-safe/liboqs-java/), [.NET](https://github.com/open-quantum-safe/liboqs-dotnet/), [Python](https://github.com/open-quantum-safe/liboqs-python/), and [Rust](https://github.com/open-quantum-safe/liboqs-rust/).  Note that these language wrappers only expose the basic algorithm APIs for directly calling; they do not integrate the PQ algorithms into higher level cryptographic APIs of the language (for example, liboqs-java let's you directly call the key generation, sign, and verify algorithms of a PQ signature scheme, but does not add support for PQ algorithms to Java's X.509 layer or Java's TLS layer.)

### How can I use post-quantum cryptography on my website and in my web browser?

In our [OQS Demos](https://github.com/open-quantum-safe/oqs-demos/), we provide example Docker images for running web server and web browser demos using post-quantum algorithms.  We also operate a [test web server](https://test.openquantumsafe.org/) for testing post-quantum TLS connections.

However, post-quantum cryptography has not yet been fully deployed in mainstream web servers and web browsers.  Google Chrome is [starting](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html) to roll out support for hybrid post-quantum cryptography, so it may be available in some users' browsers.  Most web servers do not yet support post-quantum cryptography, but some big providers and content distribution networks do, such as Cloudflare [1](https://blog.cloudflare.com/post-quantum-for-all/), [2](https://blog.cloudflare.com/post-quantum-to-origins/).

### How can I get involved?

All of our development takes place on our [GitHub repositories](https://github.com/open-quantum-safe/). Stop on by, we'd love to hear from you!
