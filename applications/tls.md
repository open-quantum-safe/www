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


We've integrated liboqs into forks of BoringSSL and OpenSSL1.1.1 as well as a standalone OQS provider for OpenSSL3 to provide prototype post-quantum key exchange and authentication and ciphersuites in the TLS protocol.  Researchers looking to try additional post-quantum algorithms can easily add more algorithms that follow the OQS API.  You can use our modified implementations to prototype quantum-resistant cryptography in applications that rely on OpenSSL (such as <a href="https://github.com/open-quantum-safe/oqs-demos/tree/main/httpd">Apache httpd</a>, <a href="https://github.com/open-quantum-safe/oqs-demos/tree/main/nginx">nginx</a>, <a href="https://github.com/open-quantum-safe/oqs-demos/tree/main/haproxy">haproxy</a>, <a href="https://github.com/open-quantum-safe/oqs-demos/tree/main/curl">curl</a>, or <a href="https://www.microsoft.com/en-us/research/project/post-quantum-crypto-vpn/">OpenVPN</a>) or on BoringSSL (such as <a href="https://github.com/open-quantum-safe/oqs-demos/tree/main/chromium">Chromium</a>).  

An [Internet-Draft](https://tools.ietf.org/html/draft-ietf-tls-hybrid-design-00) is available describing how the TLS 1.3 protocol was adapted to include the hybrid PQ key exchange algorithms.

The goal of these integration is to provide easy prototyping of quantum-resistant cryptography and should not be considered "production quality".  Please see more about [limitations of our prototype software](../about#limitations).

## OQS-OpenSSL provider

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/oqs-provider">OQS-provider <br>on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

The new, state-of-the-art [OpenSSLv3  architecture](https://www.openssl.org/docs/OpenSSLStrategicArchitecture.html) provides a more clean way to integrate novel algorithms into TLS1.3: A fully separate binary plug-in component independent of the main TLS logic, a [provider](https://www.openssl.org/docs/manmaster/man7/provider.html) permits integration of post-quantum algorithms into TLS1.3 without changing the core logic of OpenSSL. Along the same lines, providers extend X.509 certificate management functions provided by OpenSSL to new algorithm classes.

The <i>oqsprovider</i> is thus making all quantum-safe algorithms supported by OQS as well as their hybrid (classic/quantum-safe) variants readily available to OpenSSLv3 users and applications. It has matured to the level of being used as <a href="https://github.com/openssl/openssl/blob/master/test/README-external.md#oqsprovider-test-suite">validation test for the OpenSSL3 provider functionality</a>. This ensures that all quantum-safe algorithms supported by OQS are readily available without code changes to any installation running OpenSSLv3. All limitations/open issues are documented at <a href="https://github.com/open-quantum-safe/oqs-provider/issues">the issues tracker for the oqsprovider project</a>. Functional limitations of the different OpenSSL3 versions are documented [here](https://github.com/open-quantum-safe/oqs-provider#note-on-openssl-versions).

- [OQS-OpenSSL provider version 0.9.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.9.0) aligned with liboqs 0.13.0 (May 28, 2025) <span class="label label-green">current version</span>
- [OQS-OpenSSL provider version 0.8.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.8.0) aligned with liboqs 0.12.0 (December 24, 2024)
- [OQS-OpenSSL provider version 0.7.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.7.0) aligned with liboqs 0.11.0 (October 8, 2024)
- [OQS-OpenSSL provider version 0.6.1](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.6.1) aligned with liboqs 0.10.1 (June 14, 2024)
- [OQS-OpenSSL provider version 0.6.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.6.0) aligned with liboqs 0.10.0 (April 12, 2024)
- [OQS-OpenSSL provider version 0.5.2](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.5.2) aligned with liboqs 0.9.0 (October 21, 2023)
- [OQS-OpenSSL provider version 0.5.1](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.5.1) aligned with liboqs 0.8.0 (July 25, 2023)
- [OQS-OpenSSL provider version 0.5.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.5.0) aligned with liboqs 0.8.0 (June 9, 2023)
- [OQS-OpenSSL provider version 0.4.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.4.0) aligned with liboqs 0.7.2 (August 22, 2022) 
- [OQS-OpenSSL provider version 0.3.0](https://github.com/open-quantum-safe/oqs-provider/releases/tag/0.3.0) aligned with liboqs 0.7.1 (January 13, 2022)

## OQS-BoringSSL

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/boringssl">OQS-BoringSSL <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

Our <a href="https://github.com/open-quantum-safe/boringssl">BoringSSL</a> fork implements post-quantum and hybrid key exchange and post-quantum public key authentication in TLS 1.3.

See the [OQS-BoringSSL README](https://github.com/open-quantum-safe/boringssl/blob/master/README.md) for the list of supported algorithms and usage instructions.

### Releases
{: .no_toc }

- [OQS-BoringSSL snapshot 2025-01](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2025-01) aligned with liboqs 0.12.0 (January 21, 2025) <span class="label label-green">current version</span>
- [OQS-BoringSSL snapshot 2024-10](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2024-10) aligned with liboqs 0.11.0 (October 10, 2024)
- [OQS-BoringSSL snapshot 2023-06](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2023-06) aligned with liboqs 0.8.0 (July 4, 2023)
- [OQS-BoringSSL snapshot 2022-08](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2022-08) aligned with liboqs 0.7.2 (August 25, 2022)
- [OQS-BoringSSL snapshot 2022-01](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2022-01) aligned with liboqs 0.7.1 (January 6, 2022)
- [OQS-BoringSSL snapshot 2021-08](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2021-08) aligned with liboqs 0.7.0 (August 11, 2021)
- [OQS-BoringSSL snapshot 2021-03](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2021-03) aligned with liboqs 0.5.0 (March 26, 2021)
- [OQS-BoringSSL snapshot 2020-08](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2020-08) aligned with liboqs 0.4.0 (August 11, 2020)
- [OQS-BoringSSL snapshot 2020-07](https://github.com/open-quantum-safe/boringssl/releases/tag/OQS-BoringSSL-snapshot-2020-07) aligned with liboqs 0.3.0 (July 10, 2020)

Continued updates to OQS-BoringSSL are currently not planned due to lack of interest in this software. Statements of interest should be voiced [here](https://github.com/orgs/open-quantum-safe/discussions/1292).

## Demo integrations

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/oqs-demos">OQS-Demos <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

The easiest way to get started with experimenting with post-quantum cryptography is to use our pre-built Docker images containing post-quantum-enabled versions of the web servers [Apache httpd](#apache-httpd) and [nginx](#nginx), the [high-availability web proxy haproxy](#haproxy) or the command-line web client [curl](#curl). You can also download a pre-built binary of post-quantum-enabled [Chromium](#chromium) and [Wireshark](#wireshark).

There also exists a [post-quantum-enabled docker image for SSH](../ssh#demo-integration).

[OQS Docker images on Docker Hub](https://hub.docker.com/search?q=openquantumsafe&type=image){: .btn .btn-blue }

### HTTP(s) servers
{: .no_toc }

Using [our fork of OpenSSL](#oqs-openssl), we've enabled support for post-quantum and hybrid key exchange and authentication in the Apache httpd web server, the nginx web server and the haproxy load balancer.  There are links below to instructions on how to use the pre-built Docker images, or you can build your own.

### Apache httpd

- [Getting and running the pre-built post-quantum enabled **Apache httpd** demo Docker image](https://hub.docker.com/r/openquantumsafe/httpd)
- [Building your own Apache httpd demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/httpd)

### nginx

- [Getting and running the pre-built post-quantum enabled **nginx** demo Docker image](https://hub.docker.com/r/openquantumsafe/nginx)
- [Building your own nginx demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/nginx)

### haproxy

- [Getting and running the pre-built post-quantum enabled **haproxy** demo Docker image](https://hub.docker.com/r/openquantumsafe/haproxy)
- [Building your own haproxy demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/haproxy)

### HTTP(s) clients
{: .no_toc }

Using our forks of [OpenSSL](#oqs-openssl) and [BoringSSL](#oqs-boringssl), we've enabled support for post-quantum and hybrid key exchange and authentication in the curl command-line web client and the Chromium and Epiphany web browsers.

### curl

- [Getting and running the pre-built post-quantum enabled **curl** demo Docker image](https://hub.docker.com/r/openquantumsafe/curl)
- [Building your own curl demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/curl)

### Chromium

- [Pre-built Chromium binary for Ubuntu 20.04 (64bit x86) at liboqs v0.7.2](https://github.com/open-quantum-safe/oqs-demos/releases/download/0.7.2/chromium-ubuntu-0.7.2.tgz) (149 MB)
- [Building your own Chromium binary](https://github.com/open-quantum-safe/oqs-demos/tree/main/chromium) (warning: painful!)

### epiphany

- [Getting and running the pre-built post-quantum enabled **epiphany** browser demo Docker image](https://hub.docker.com/r/openquantumsafe/epiphany)
- [Building your own epiphany demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/epiphany)


### Wireshark

- [Getting and running the pre-built post-quantum enabled **Wireshark** demo Docker image](https://hub.docker.com/repository/docker/openquantumsafe/wireshark) and [usage instructions](https://github.com/open-quantum-safe/oqs-demos/blob/main/wireshark/USAGE.md)
- [Building your own Wireshark demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/wireshark)

### (Interoperability) Test server

We're interested in design and draft standards for hybrid authentication and key exchange as well as interoperability testing with other implementers. As an initial step to facilitate such testing we have set up a first iteration of such a demonstration and interoperability test server at [https://test.openquantumsafe.org](https://test.openquantumsafe.org). All of the clients above can be used with this test server using [the above post-quantum enabled nginx](#nginx). Any usage and all feedback is very welcome.

[Test server](https://test.openquantumsafe.org/){: .btn .btn-blue }

### QUIC

The [QUIC](https://www.rfc-editor.org/rfc/rfc9000.html) protocol uses TLS1.3 for secure session establishment. We thus could also make available post-quantum enabled **QUIC** client and server components:

- [Getting and running the pre-built post-quantum enabled **nginx-quic** demo Docker image](https://hub.docker.com/repository/docker/openquantumsafe/nginx-quic)
- [Getting and running the pre-built post-quantum enabled **msquic** (reach) demo Docker image](https://hub.docker.com/repository/docker/openquantumsafe/msquic-reach)
- [Building your own QUIC-enabled client- and server components](https://github.com/open-quantum-safe/oqs-demos/tree/main/quic)
- [Additional Dockerfiles exist to provide post-quantum enablement](https://github.com/open-quantum-safe/oqs-demos/tree/main/ngtcp2) for [ngtcp2](https://github.com/ngtcp2/ngtcp2).

*Note*: This code is still based on `oqs-openssl111` thus may become unsupported as soon as [OpenSSL1.1.1 support ends in September 2023](https://www.openssl.org/blog/blog/2023/03/28/1.1.1-EOL).

### MQTT

The [MQTT](https://mqtt.org) protocol also uses TLS for session security. We thus could also make available post-quantum enabled **MQTT** broker, subscriber and publisher based on [Mosquitto](https://mosquitto.org/):

- [Getting and running pre-built quantum-safe Mosquitto docker images](https://hub.docker.com/repository/docker/openquantumsafe/mosquitto).
- [Building your own quantum safe Mosquitto docker images](https://github.com/open-quantum-safe/oqs-demos/tree/main/mosquitto).

*Note*: This code is still based on `oqs-openssl111` thus may become unsupported as soon as [OpenSSL1.1.1 support ends in September 2023](https://www.openssl.org/blog/blog/2023/03/28/1.1.1-EOL).

## Discontinued projects

### OQS-OpenSSL

{: .warning }
<b>DEPRECATION NOTICE</b>: The OpenSSL project has stopped support for OpenSSL 1.1.1, and all users should switch to OpenSSL 3. Consequently, the Open Quantum Safe project has discontinued development of our OQS-OpenSSL 1.1.1 fork. This repository is archived as read-only. Use of this code is not recommended, as it may rely on obsolete algorithms or implementations or may have security vulnerabilities or other bugs. The [OQS Provider for OpenSSL 3](https://github.com/open-quantum-safe/oqs-provider/) provides full support for post-quantum key exchange and authentication in TLS 1.3, X.509, and S/MIME. 

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/openssl">OQS-OpenSSL <br>on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

The OQS-OpenSSL-1.1.1 fork provided post-quantum and hybrid key exchange and post-quantum public key authentication in TLS 1.3, and post-quantum algorithms in X.509 certificate generation and S/MIME / CMS message handling.

<details markdown="block">
<summary>Click here to see archived OQS-OpenSSL 1.1.1 releases</summary>
- [OQS-OpenSSL 1.1.1 snapshot 2023-07](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL-1_1_1-stable-snapshot-2023-07) aligned with liboqs 0.8.0 (July 7, 2023) <span class="label label-red">deprecated</span>
- [OQS-OpenSSL 1.1.1 snapshot 2022-08](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL-1_1_1-stable-snapshot-2022-08) aligned with liboqs 0.7.2 (August 24, 2022)
- [OQS-OpenSSL 1.1.1 snapshot 2022-01](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2022-01) aligned with liboqs 0.7.1 (January 6, 2022)
- [OQS-OpenSSL 1.1.1 snapshot 2021-08](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2021-08) aligned with liboqs 0.7.0 (August 11, 2021)
- [OQS-OpenSSL 1.1.1 snapshot 2021-03](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2021-03) aligned with liboqs 0.5.0 (March 26, 2021)
- [OQS-OpenSSL 1.1.1 snapshot 2020-08](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2020-08) aligned with liboqs 0.4.0 (August 11, 2020)
- [OQS-OpenSSL 1.1.1 snapshot 2020-07](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2020-07) aligned with liboqs 0.3.0 (July 10, 2020)
- [OQS-OpenSSL 1.1.1 snapshot 2019-10](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2019-10) aligned with liboqs 0.2.0 (October 8, 2019)
- [OQS-OpenSSL 1.1.1 snapshot 2018-11](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_1_1-stable-snapshot-2018-11) aligned with liboqs 0.1.0 (November 13, 2018)
- [all releases](https://github.com/open-quantum-safe/liboqs/releases)
</details>

The OQS-OpenSSL-1.0.2 fork provided post-quantum and hybrid algorithms in TLS 1.2.

<details markdown="block">
<summary>Click here to see archived OQS-OpenSSL 1.0.2 releases</summary>
- [OQS-OpenSSL 1.0.2 snapshot 2019-10](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2019-10) aligned with liboqs 0.2.0 (October 8, 2019) <span class="label label-red">deprecated</span>
- [OQS-OpenSSL 1.0.2 snapshot 2018-11](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2018-11) aligned with liboqs 0.1.0 (November 13, 2018)
- [OQS-OpenSSL 1.0.2 snapshot 2018-05](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2018-05) (May 30, 2018)
- [OQS-OpenSSL 1.0.2 snapshot 2018-04](https://github.com/open-quantum-safe/openssl/releases/tag/OQS-OpenSSL_1_0_2-stable-snapshot-2018-04) (April 10, 2018)
</details>

### OQS-Engine

{: .warning }
<b>DEPRECATION NOTICE</b>: Maintenance of the OQS-Engine has been discontinued as of April 2021. This repository is archived as read-only. Use of this code is not recommended, as it may rely on obsolete algorithms or implementations or may have security vulnerabilities or other bugs. The [OQS Provider for OpenSSL 3](https://github.com/open-quantum-safe/oqs-provider/) provides full support for post-quantum key exchange and authentication in TLS 1.3, X.509, and S/MIME. 

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/oqs-engine">OQS-Engine <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

<a href="https://github.com/open-quantum-safe/oqs-engine">oqs-engine</a> was a C-based OpenSSL engine that enables in (vanilla) OpenSSL the use of post-quantum digital signature algorithms from liboqs. We are grateful to <a href="https://www.senetas.com">Senetas</a> for contributing this engine to the OQS project.  Hear about Senetas' work on the engine for OQS in their interview on <a href="https://risky.biz/RB581/">episode 581 of the Risky Business podcast</a>.
