---
layout: default
parent: Research
title: Benchmarking post-quantum cryptography in TLS
nav_exclude: true
---

# Benchmarking post-quantum cryptography in TLS

Christian Paquin, Douglas Stebila, Goutam Tamvada. **Benchmarking post-quantum cryptography in TLS**. In Jintai Ding, Jean-Pierre Tillich, editors, *Proc. 11th International Conference on Post-Quantum Cryptography (PQCrypto) 2020*, *LNCS*, vol. 12100, pp. 72-91. Springer, April 2020. © Springer.

## Abstract

<div class="float float-right"><a href="https://www.douglas.stebila.ca/files/research/papers/PQCrypto-PaqSteTam20.pdf"><img src="https://www.douglas.stebila.ca/files/research/images/papers/PQCrypto-PaqSteTam20-chart.png" width="300px"></a></div>

Post-quantum cryptographic primitives have a range of trade-offs compared to traditional public key algorithms, either having slower computation or larger public keys and ciphertexts/signatures, or both. While the performance of these algorithms in isolation is easy to measure and has been a focus of optimization techniques, performance in realistic network conditions has been less studied. Google and Cloudflare have reported results from running experiments with post-quantum key exchange algorithms in the Transport Layer Security (TLS) protocol with real users' network traffic. Such experiments are highly realistic, but cannot be replicated without access to Internet-scale infrastructure, and do not allow for isolating the effect of individual network characteristics.

In this work, we develop and make use of a framework for running such experiments in TLS cheaply by emulating network conditions using networking features of the Linux kernel. Our testbed allows us to independently control variables such as link latency and packet loss rate, and then examine the impact on TLS connection establishment performance of various post-quantum primitives, specifically hybrid elliptic curve/post-quantum key exchange and post-quantum digital signatures, based on implementations from the Open Quantum Safe project. Among our key results, we observe that packet loss rates above 3-5% start to have a significant impact on post-quantum algorithms that fragment across many packets, such as those based on unstructured lattices. The results from this emulation framework are also complemented by results on the latency of loading entire web pages over TLS in real network conditions, which show that network latency hides most of impact from algorithms with slower computations (such as supersingular isogenies).

## Download

- <a class="btn btn-primary" href="https://www.douglas.stebila.ca/files/research/papers/PQCrypto-PaqSteTam20.pdf">Full version (PDF)</a>
- [Publisher's website](https://doi.org/10.1007/978-3-030-44223-1_5)
- [IACR Cryptology ePrint Archive report 2019/1447](https://eprint.iacr.org/2019/1447)

## Presentations
- 2020-02-07: [Netherlands Crypto Workshop](https://www.douglas.stebila.ca/files/research/presentations/20200207-Netherlands.pdf)
- 2019-12-17: [Grenoble Alpes Cybersecurity Institute Workshop on Post-Quantum Cryptography](https://www.douglas.stebila.ca/files/research/presentations/20191217-Univ-Grenoble.pdf)
- 2019-12-13: [IBM Research Zurich](https://www.douglas.stebila.ca/files/research/presentations/20191213-IBM-Zurich.pdf)

## BibTeX

```bibtex
@inproceedings{PQCrypto:PaqSteTam20,
	Author = {Christian Paquin and Douglas Stebila and Goutam Tamvada},
	Booktitle = {Proc. 11th International Conference on Post-Quantum Cryptography (PQCrypto) 2020},
	Editor = {Jintai Ding and Jean-Pierre Tillich},
	Month = {April},
	Pages = {72--91},
	Publisher = {Springer},
	Series = {LNCS},
	Title = {Benchmarking post-quantum cryptography in {TLS}},
	Volume = {12100},
	Year = {2020}
}
```

## Funding

This research was supported by:

- Natural Sciences and Engineering Research Council of Canada (NSERC) Discovery grant RGPIN-2016-05146
- NSERC Discovery Accelerator Supplement grant RGPIN-2016-05146
