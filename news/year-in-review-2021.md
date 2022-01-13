---
layout: default
title: Year in review – 2021
nav_order: 3
has_children: false
has_toc: true
parent: About our project
---
# Year in review – 2021

*January, 2022*

## Software releases

In 2021 we focused on updating our software for Round 3 of the NIST Post-Quantum Crypto standardization project and supporting additional architectures.  The core of our project remains the **liboqs** C library.

In July 2020, NIST announced selected 15 algorithms to advance to Round 3, with a deadline for updated submissions in October 2020.  In liboqs 0.5.0, released in March 2021, we removed algorithms eliminated from Round 2 and began updating to Round 3 implementations, the first of 4 releases of liboqs in 2021.  Our most recently release, liboqs 0.7.1 in December 2021, currently supports all Round 3 finalists and alternate candidates, except for one (GeMSS).

We improved support for building liboqs on more architectures, enhancing the build system to better detect CPU features available for optimized implementations.  Our primary platforms remain x86\_64 and ARMv8, but we also added preliminary support for building on ppc64le, x86, and S390x.  We added more optimized code for ARM platforms supporting crypto extensions and NEON, including Apple Silicon.  We also extended our testing suite to use Valgrind to check for secret-dependent branching; not all implementations currently avoid secret-dependent branching, but exceptions are documented.  We added ARM builds to our profiling dashboard.

We made three snapshot releases of **OQS-OpenSSL-1.1.1** to incorporate updates of the main OpenSSL project and synchronize with algorithms added in liboqs releases.  We similarly updated **OQS-BoringSSL**.  This year we introduced a new TLS-related subproject, **oqs-provider**, led by Michael Baentsch, with financial support from the NLnet NGI Assure fund.  oqs-provider utilizes the OpenSSL 3 provider architecture to add post-quantum algorithms to OpenSSL 3-reliant applications at run-time.  oqs-provider adds post-quantum and hybrid key exchange to TLS 1.3, as well as post-quantum signatures in the OpenSSL envelope (EVP) API, all built on liboqs and fully compatible with our OQS-OpenSSL and OQS-BoringSSL implementations.  We continue to make available an interoperability test server for our TLS 1.3 post-quantum algorithms.

We also made two snapshot releases of **OQS-OpenSSH**, including a full rewrite by Christian Paquin and Goutam Tamvada to update to the OpenSSH v8 release series.  Kevin Kane of Microsoft Research developed and contributed a new OQS subproject, **OQS-libssh**, which is a fork of the libssh library that includes prototype quantum-resistant key exchange and authentication based on liboqs.

We continued to update our **language-specific SDKs** to reflect algorithm updates in liboqs, and currently have wrappers available for **C++, Go, Java, .NET, Python, and Rust**.

The **oqs-demos** subproject continues to make available instructions and binaries/Docker images for a variety of applications, including **curl, Apache httpd, nginx, Chromium, and HAproxy**.  In 2021, we added Docker images for OQS-OpenSSH, contributed by the ISE group at Fachhochschule Nordwestschweiz, and a Docker image containing a version of **Wireshark** that recognizes post-quantum and hybrid TLS handshakes, contributed by Anthony Hu of wolfSSL.

## Impact

In 2021 we were very pleased to see renewed external interest in the tools created by the Open Quantum Safe project.  liboqs was made available to **FreeBSD** users via the FreeBSD ports system, and to **Debian** users as a new package in the Debian unstable branch.  Several open source crypto libraries have started experiments based on liboqs, including prototype experiments in ARM's **mbed TLS** library and a wide-ranging set of experiments by **wolfSSL**.  We also learned about an experiment by National Grid that used OQS-OpenSSL to build a post-quantum-enabled version of the GNOME web browser (Epiphany).

In June 2021 we presented an update on the Open Quantum Safe project at Third NIST PQC Standardization Conference.  OQS team members also gave presentations at the following conferences and seminar series:

- Alphabet
- Cryptology and Network Security (CANS) 2021
- Dell/VMWare PQC Forum
- International Cryptographic Module Conference (ICMC) 2021
- Internet Engineering Task Force (IETF) 111 TLS Working Group
- Post-Quantum Networks Workshop
- Storage Developer Conference (SDC) 2021
- University of Surrey

## Contributors and Partners

Members of our **core team** in 2021 were: Michael Baentsch (baentsch.ch), Eric Crockett (Amazon Web Services), Vlad Gheorghiu (softwareQ / University of Waterloo), Basil Hess (IBM Research), Christian Paquin (Microsoft Research), John Schanck (University of Waterloo), Douglas Stebila (University of Waterloo), and Goutam Tamvada (University of Waterloo).

We are very pleased to acknowledge ongoing participation and support from the teams at **Amazon Web Services**, **evolutionQ**, **IBM Research**, and **Microsoft Research**.  

We continue to co-operate closely with the **PQClean project** which provides many of the implementatations of post-quantum algorithms used in liboqs.

In 2021 we received financial support for OQS from **Amazon Web Services**, the **Canadian Centre for Cyber Security**, the **NLnet NGI Assure fund**, and the **Unitary Fund**.  Research projects based on OQS were supported by funding from the **Natural Sciences and Engineering Research Council of Canada (NSERC)**. **Microsoft Research** donated computation time on Azure.

We'd like to acknowledge new contributors to OQS in 2021: Fabien Benetou, Sofía Celi, Vitaly Chikunov, Ted Eaton, Jason Goertzen, Hannes (Github: umgefahren), Philip Haynes, Anthony Hu, Dusan Kostic, Piotr Kubaj, Richard Levitte, Joy Osive, Julien Pierre, Sebastian Ramacher, Nico Schwab, Karolin Varner, Wiejun Wang, and Jiewen Yao.

<br>

Thanks to everyone who helped make 2021 a great year for OQS!

*Douglas Stebila* <br>
*Project leader, Open Quantum Safe project*
