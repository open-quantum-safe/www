---
layout: default
parent: Applications and protocols
title: TLS
nav_order: 1
has_children: false
has_toc: false
---

# TLS
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


We've integrated liboqs into forks of BoringSSL and OpenSSL to provide prototype post-quantum key exchange and authentication and ciphersuites in the TLS protocol.  Researchers looking to try additional post-quantum algorithms can easily add more algorithms that follow the OQS API.  You can use our modified implementations to prototype quantum-resistant cryptography in applications that rely on OpenSSL (such as <a href="https://github.com/open-quantum-safe/oqs-demos/tree/master/httpd">Apache httpd</a>, <a href="https://github.com/open-quantum-safe/oqs-demos/tree/master/nginx">nginx</a>, <a href="https://github.com/open-quantum-safe/oqs-demos/tree/master/curl">curl</a>, or <a href="https://www.microsoft.com/en-us/research/project/post-quantum-crypto-vpn/">OpenVPN</a>) or on BoringSSL (such as <a href="https://github.com/open-quantum-safe/oqs-demos/tree/master/chromium">Chromium</a>).  

An [Internet-Draft](https://tools.ietf.org/html/draft-ietf-tls-hybrid-design-00) is available describing how the TLS 1.3 protocol was adapted to include the hybrid PQ key exchange algorithms.

The goal of these integration is to provide easy prototyping of quantum-resistant cryptography and should not be considered "production quality".  Please see more about [limitations of our prototype software](../about).

## OQS-OpenSSL

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/openssl">OQS-OpenSSL <br>on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

Our <a href="https://github.com/open-quantum-safe/openssl">OpenSSL fork</a> implements post-quantum and hybrid key exchange and post-quantum public key authentication in TLS 1.3, and also supports post-quantum algorithms in X.509 certificate generation and S/MIME / CMS message handling.

See the [OQS-OpenSSL README](https://github.com/open-quantum-safe/openssl/blob/OQS-OpenSSL_1_1_1-stable/README.md) for the list of supported algorithms and usage instructions.

### Releases
{: .no_toc }

The OQS-OpenSSL-1.1.1 series provides post-quantum algorithms in TLS 1.3, X.509, and S/MIME:

- [OQS-OpenSSL 1.1.1 snapshot 2020-08](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2020-08) aligned with liboqs 0.4.0 (August 11, 2020) <span class="label label-green">current version</span>
- [OQS-OpenSSL 1.1.1 snapshot 2020-07](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2020-07) aligned with liboqs 0.3.0 (July 10, 2020)
- [OQS-OpenSSL 1.1.1 snapshot 2019-10](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2019-10) aligned with liboqs 0.2.0 (October 8, 2019)
- [OQS-OpenSSL 1.1.1 snapshot 2018-11](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2018-11) aligned with liboqs 0.1.0 (November 13, 2018)
- [all releases](https://github.com/open-quantum-safe/liboqs/releases)

The OQS-OpenSSL-1.0.2 series provided post-quantum algorithms in TLS 1.2.  It is deprecated and no longer maintained.

<details markdown="block">
<summary>OQS-OpenSSL 1.0.2 releases</summary>
- [OQS-OpenSSL 1.0.2 snapshot 2019-10](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2019-10) aligned with liboqs 0.2.0 (October 8, 2019)
- [OQS-OpenSSL 1.0.2 snapshot 2018-11](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2018-11) aligned with liboqs 0.1.0 (November 13, 2018)
- [OQS-OpenSSL 1.0.2 snapshot 2018-05](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2018-05) (May 30, 2018)
- [OQS-OpenSSL 1.0.2 snapshot 2018-04](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2018-04) (April 10, 2018)
</details>

## OQS-BoringSSL

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/boringssl">OQS-BoringSSL <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

Our <a href="https://github.com/open-quantum-safe/boringssl">BoringSSL</a> fork implements post-quantum and hybrid key exchange and post-quantum public key authentication in TLS 1.3.

See the [OQS-BoringSSL README](https://github.com/open-quantum-safe/boringssl/blob/master/README.md) for the list of supported algorithms and usage instructions.

### Releases
{: .no_toc }

- [OQS-BoringSSL snapshot 2020-08](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2020-08) aligned with liboqs 0.4.0 (August 11, 2020) <span class="label label-green">current version</span>
- [OQS-BoringSSL snapshot 2020-07](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2020-07) aligned with liboqs 0.3.0 (July 10, 2020)

## OQS-Engine

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/oqs-engine">OQS-Engine <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

<a href="https://github.com/open-quantum-safe/oqs-engine">oqs-engine</a> is a C-based OpenSSL ENGINE that enables in (vanilla) OpenSSL the use of post-quantum digital signature algorithms from liboqs. Changes and/or additions to the algorithms supported by liboqs will be dynamically reflected in the ENGINE, thereby facilitating the deployment and evaluation of post-quantum digital signature algorithms in contexts where it might be expensive or infeasible to replace OpenSSL wholesale with our corresponding fork. 

We are grateful to <a href="https://www.senetas.com">Senetas</a> for contributing this ENGINE to the OQS project.  Hear about Senetas' work on the ENGINE for OQS in their interview on <a href="https://risky.biz/RB581/">episode 581 of the Risky Business podcast</a>.

## Demos

The easiest way to get started with experimenting with post-quantum cryptography is to use our pre-built Docker images containing post-quantum-enabled versions of the web servers Apache httpd and nginx, or the command-line web client curl.  You can also download a pre-built binary of post-quantum-enabled Chromium.

[Demo Docker images](https://github.com/open-quantum-safe/oqs-demos/){: .btn .btn-blue }

### HTTP servers: Apache httpd and nginx

Using [our fork of OpenSSL](#oqs-openssl), we've enabled support for post-quantum and hybrid key exchange and authentication in the Apache httpd web server and the nginx web server.  There are links below to instructions on how to use the pre-built Docker images, or you can build your own.

- **Apache httpd**
    - [Getting and running the pre-built post-quantum enabled **Apache httpd** demo Docker image](https://github.com/open-quantum-safe/oqs-demos/blob/master/httpd/USAGE.md)
    - [Building your own Apache httpd demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/master/httpd)
- **nginx**
    - [Getting and running the pre-built post-quantum enabled **nignx** demo Docker image](https://github.com/open-quantum-safe/oqs-demos/blob/master/nginx/USAGE.md)
    - [Building your own nginx demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/master/nginx)

### HTTP clients: curl and Chromium

Using our forks of [OpenSSL](#oqs-openssl) and [BoringSSL](#oqs-boringssl), we've enabled support for post-quantum and hybrid key exchange and authentication in the curl command-line web client and the Chromium web browser.

- **curl**
    - [Getting and running the pre-built post-quantum enabled **curl** demo Docker image](https://github.com/open-quantum-safe/oqs-demos/blob/master/curl/USAGE.md)
    - [Building your own curl demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/master/curl)
- **Chromium**
    - [Pre-built Chromium binary for Ubuntu 18.04](https://github.com/open-quantum-safe/oqs-demos/releases/download/v0.4.0/chromium-ubuntu-0.4.0.tgz) (149 MB)
    - [Building your own Chromium binary](https://github.com/open-quantum-safe/oqs-demos/tree/master/chromium) (warning: painful!)

### Test server

We're interested in design and draft standards for hybrid authentication and key exchange as well as interoperability testing with other implementers. As an initial step to facilitate such testing we have set up a first iteration of such a demonstration and interoperability test server. All of the clients above can be used with this test server. Any usage and all feedback is very welcome.

[Test server](https://test.openquantumsafe.org/){: .btn .btn-blue }
