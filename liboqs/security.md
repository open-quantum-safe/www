---
layout: default
parent: liboqs
title: Security policy
nav_order: 3
---

# Security policy

The [liboqs security policy document](https://github.com/open-quantum-safe/liboqs/blob/main/SECURITY.md) lists the supported versions of liboqs and describes the threat model that liboqs aims to protect against.  

Security reports for liboqs will be handled in accordance with the [OQS security response process](https://github.com/open-quantum-safe/tsc/blob/main/security/response-process.md).

## Reporting security bugs

If you think you have found a security bug in OQS software, please send email to security@openquantumsafe.org or submit a security disclosure on Github for [liboqs](https://github.com/open-quantum-safe/liboqs/security) or [oqs-provider](https://github.com/open-quantum-safe/oqs-provider/security).  

We do not run a bug bounty program.

## General principles

We do aim to create reliable, secure software implementing post-quantum cryptography.  However, we are primarily a research project focused on prototyping and evaluating post-quantum cryptography, not on creating products, so our response to security issues will be on a best-effort basis, and we do not make guarantees on timelines.  Note that many algorithm implementations included in OQS are obtained from other projects; resolving issues may require coordination with other parties and this may affect resolution time.

Note that a cryptanalytic flaw in an algorithm may result in an algorithm being temporarily removed until its creators issue a fix, or permanently removed if broken.

The goal of these integration is to provide easy prototyping of quantum-resistant cryptography and should not be considered "production quality".  Please see more about [limitations of our prototype software](../about#limitations).

## Notification

When we are planning an update that fixes a high severity security issue, we will post an update on our website openquantumsafe.org indicating a planned release date and will notify those who have requested to be added to our notification list (oqs-security-annnounce@lists.pqca.org); [click here to sign up for the security notification list](https://lists.pqca.org/g/oqs-security-announce/). 

## Security audits and reviews

Trail of Bits carried out a review of portions of liboqs in 2024.  Their report can be found at [https://github.com/trailofbits/publications/blob/master/reviews/2025-04-quantum-open-safe-liboqs-securityreview.pdf](https://github.com/trailofbits/publications/blob/master/reviews/2025-04-quantum-open-safe-liboqs-securityreview.pdf).
