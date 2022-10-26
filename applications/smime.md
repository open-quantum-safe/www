---
layout: default
parent: Applications and protocols
title: CMS and S/MIME
nav_order: 4
---

# CMS and S/MIME

Our [fork of OpenSSL](tls/#oqs-openssl) as well as [oqsprovider](tls.html#oqs-openssl-provider) together with OpenSSL3 (master) can perform S/MIME and CMS signing operations using post-quantum and hybrid digital signatures.

For instructions on doing post-quantum S/MIME operations, see the [OQS-OpenSSL README section "CMS demo"](https://github.com/open-quantum-safe/openssl/blob/OQS-OpenSSL_1_1_1-stable/README.md#cms-demo).

The easiest way to execute post-quantum S/MIME and CMS signing operations is by [using the pre-built openssl 1.1.1 docker image at Docker hub](https://hub.docker.com/r/openquantumsafe/curl) or [using the pre-built OpenSSL3 docker image at Docker hub](https://hub.docker.com/repository/docker/openquantumsafe/oqs-ossl3).

Information on post-quantum X.509 certificates can be found [here](x509).
