---
layout: default
parent: Applications and protocols
title: SSH
nav_order: 2
---

# SSH

## OQS-OpenSSH

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/openssh">OQS-OpenSSH <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

We've integrated liboqs into a fork of OpenSSH to provide prototype post-quantum and hybrid key exchange in the SSH protocol.  Researchers looking to try additional post-quantum algorithms can easily add more algorithms that follow the OQS API.  

A [pre-Internet-Draft](https://github.com/open-quantum-safe/openssh/blob/OQS-master/ietf_pre_draft_sike_bike_hybrid_kex.txt) is available describing how the SSH protocol was adapted to include the hybrid PQ key exchange algorithms.

The goal of this integration is to provide easy prototyping of quantum-resistant cryptography and should not be considered "production quality".  Please see more about [limitations of our prototype software](../about#limitations).

See the [README](https://github.com/open-quantum-safe/openssh/blob/OQS-master/README.md) for the list of supported algorithms and usage instructions.

### Demo integration

<div class="float-right"><a class="btn btn-purple" href="https://github.com/open-quantum-safe/oqs-demos">OQS-Demos <br> on Github <img src="{{ site.baseurl }}/img/logos/GitHub-Mark-Light-64px.png" style="height: 1em; padding-left: 1em; margin-bottom: -2px;"></a></div>

The easiest way to get started with experimenting with post-quantum cryptography is to use our pre-built Docker image containing post-quantum-enabled openssh:

- [Getting and running the pre-built post-quantum enabled **openssh** demo Docker image](https://hub.docker.com/r/openquantumsafe/openssh)
- [Building your own openssh demo Docker image](https://github.com/open-quantum-safe/oqs-demos/tree/main/openssh)

There also exist [post-quantum-enabled docker images for TLS applications](../tls#demo-integrations).

### Releases

- [snapshot 2020-08](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2020-08) aligned with liboqs 0.4.0 (September 3, 2020) <span class="label label-green">current version</span>
- [snapshot 2020-07](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2020-07) aligned with liboqs 0.3.0 (July 10, 2020)
- [snapshot 0219-10](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2019-10) aligned with liboqs 0.2.0 (October 8, 2019)
- [snapshot 2020-07](https://github.com/open-quantum-safe/openssh/releases/tag/OQS-OpenSSH-snapshot-2018-11) aligned with liboqs 0.1.0 (November 13, 2018)
- [all releases](https://github.com/open-quantum-safe/liboqs/releases)

### Acknowledgements

The current OQS-OpenSSH fork was originally developed by Torben Hansen (Amazon Web Services and Royal Holloway, University of London), and is now maintained by [the OQS team](https://github.com/open-quantum-safe/openssh/blob/OQS-master/README.md#team).
