---
layout: default
parent: Applications and protocols
title: SSH
nav_order: 2
---

# SSH
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


We've integrated liboqs into forks of OpenSSH and libssh to provide prototype post-quantum and hybrid key exchange in the SSH protocol.  Researchers looking to try additional post-quantum algorithms can easily add more algorithms that follow the OQS API.

A [pre-Internet-Draft](https://github.com/open-quantum-safe/openssh/blob/OQS-master/ietf_pre_draft_sike_bike_hybrid_kex.txt) is available describing how the SSH protocol was adapted to include the hybrid PQ key exchange algorithms.

The goal of these integrations is to provide easy prototyping of quantum-resistant cryptography and should not be considered "production quality".  Please see more about [limitations of our prototype software](../about#limitations).

{: .warning }
<b>Note:</b> Our OpenSSH and libssh integrations are currently inactive and not receiving updates. Contributors are welcome.

## OQS-OpenSSH

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/openssh">OQS-OpenSSH <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

Our <a href="https://github.com/open-quantum-safe/openssh">OpenSSH fork</a> implements post-quantum and hybrid key exchange in the SSH protocol.
See the [README](https://github.com/open-quantum-safe/openssh/blob/OQS-master/README.md) for the list of supported algorithms and usage instructions.

### Demo integration
{: .no_toc }

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/oqs-demos">OQS-Demos <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

The easiest way to get started with experimenting with post-quantum cryptography is to use our pre-built Docker image containing post-quantum-enabled openssh:

- [Getting and running the pre-built post-quantum enabled **openssh** demo Docker image](https://hub.docker.com/r/openquantumsafe/openssh)
- [Building your own openssh demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/openssh)

There also exist [post-quantum-enabled docker images for TLS applications](tls#demo-integrations).

### Releases
{: .no_toc }

- [snapshot 2023-10](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2023-06) aligned with liboqs 0.9.0 (October 21, 2023) <span class="label label-green">current version</span>
- [snapshot 2023-06](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2023-06) aligned with liboqs 0.8.0 (June 26, 2023) 
- [snapshot 2022-08](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2022-08) aligned with liboqs 0.7.2 (August 23, 2022)
- [snapshot 2022-01](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2022-01) aligned with liboqs 0.7.1 (January 6, 2022)
- [snapshot 2021-08](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2021-08) aligned with liboqs 0.7.0 (August 11, 2021)
- [snapshot 2020-08](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2020-08) aligned with liboqs 0.4.0 (September 3, 2020)
- [snapshot 2020-07](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2020-07) aligned with liboqs 0.3.0 (July 10, 2020)
- [snapshot 0219-10](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2019-10) aligned with liboqs 0.2.0 (October 8, 2019)
- [snapshot 2020-07](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2018-11) aligned with liboqs 0.1.0 (November 13, 2018)
- [all releases](https://github.com/open-quantum-safe/liboqs/releases)

## OQS-libssh

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/libssh">OQS-libssh <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

Our <a href="https://github.com/open-quantum-safe/libssh">libssh fork</a> implements post-quantum and hybrid key exchange in the SSH protocol.
See the [README](https://github.com/open-quantum-safe/libssh/blob/OQS-master/README.md) for the list of supported algorithms and usage instructions.

### Releases
{: .no_toc }

- [snapshot 2022-01](https://github.com/open-quantum-safe/libssh/releases/tag/OQS-libssh-snapshot-2022-01) aligned with liboqs 0.7.1 (January 25, 2022) <span class="label label-green">current version</span>
