---
layout: default
parent: liboqs
title: Algorithms
nav_order: 2
---

# Algorithms in liboqs

## Key encapsulation mechanisms (KEMs)

### Round 3 finalists

- [**Classic McEliece**](kem/classic_mceliece): Classic-McEliece-348864†, Classic-McEliece-348864f†, Classic-McEliece-460896†, Classic-McEliece-460896f†, Classic-McEliece-6688128†, Classic-McEliece-6688128f†, Classic-McEliece-6960119†, Classic-McEliece-6960119f†, Classic-McEliece-8192128†, Classic-McEliece-8192128f†
- [**Kyber**](kem/kyber): Kyber512, Kyber768, Kyber1024, Kyber512-90s, Kyber768-90s, Kyber1024-90s
- [**NTRU**](kem/ntru): NTRU-HPS-2048-509, NTRU-HPS-2048-677, NTRU-HPS-4096-821, NTRU-HPS-4096-1229, NTRU-HRSS-701, NTRU-HRSS-1373
- [**SABER**](kem/saber): LightSaber-KEM, Saber-KEM, FireSaber-KEM

<small>Note that algorithms marked with a dagger (†) have large stack usage and may cause failures when run on threads or in constrained environments.</small>

### Round 3 alternate candidates

- [**BIKE**](kem/bike): BIKE1-L1-CPA, BIKE1-L3-CPA, BIKE1-L1-FO, BIKE1-L3-FO
- [**FrodoKEM**](kem/frodokem): FrodoKEM-640-AES, FrodoKEM-640-SHAKE, FrodoKEM-976-AES, FrodoKEM-976-SHAKE, FrodoKEM-1344-AES, FrodoKEM-1344-SHAKE
- [**HQC**](kem/hqc): HQC-128-1-CCA2, HQC-192-1-CCA2, HQC-192-2-CCA2, HQC-256-1-CCA2†, HQC-256-2-CCA2†, HQC-256-3-CCA2†
- [**NTRU-Prime**](kem/ntruprime): ntrulpr653, ntrulpr761, ntrulpr857, ntrulpr1277, sntrup653, sntrup761, sntrup857, sntrup1277

## Signature schemes

### Round 3 finalists

- [**Dilithium**](sig/dilithium): Dilithium2, Dilithium2-AES, Dilithium3, Dilithium3-AES, Dilithium5, Dilithium5-AES
- [**Falcon**](sig/falcon): Falcon-512, Falcon-1024
- [**Rainbow**](sig/rainbow): Rainbow-III-Classic†, Rainbow-III-Circumzenithal†, Rainbow-III-Compressed†, Rainbow-V-Classic†, Rainbow-V-Circumzenithal†, Rainbow-V-Compressed†

<small>Note that algorithms marked with a dagger (†) have large stack usage and may cause failures when run on threads or in constrained environments.</small>

### Round 3 alternate candidates

- [**Picnic**](sig/picnic): Picnic-L1-FS, Picnic-L1-UR, Picnic-L1-full, Picnic-L3-FS, Picnic-L3-UR, Picnic-L3-full, Picnic-L5-FS, Picnic-L5-UR, Picnic-L5-full, Picnic3-L1, Picnic3-L3, Picnic3-L5
- [**SPHINCS+**](sig/sphincs):
    - **SPHINCS+-Haraka**: SPHINCS+-Haraka-128f-robust, SPHINCS+-Haraka-128f-simple, SPHINCS+-Haraka-128s-robust, SPHINCS+-Haraka-128s-simple, SPHINCS+-Haraka-192f-robust, SPHINCS+-Haraka-192f-simple, SPHINCS+-Haraka-192s-robust, SPHINCS+-Haraka-192s-simple, SPHINCS+-Haraka-256f-robust, SPHINCS+-Haraka-256f-simple, SPHINCS+-Haraka-256s-robust, SPHINCS+-Haraka-256s-simple
    - **SPHINCS+-SHA256**: SPHINCS+-SHA256-128f-robust, SPHINCS+-SHA256-128f-simple, SPHINCS+-SHA256-128s-robust, SPHINCS+-SHA256-128s-simple, SPHINCS+-SHA256-192f-robust, SPHINCS+-SHA256-192f-simple, SPHINCS+-SHA256-192s-robust, SPHINCS+-SHA256-192s-simple, SPHINCS+-SHA256-256f-robust, SPHINCS+-SHA256-256f-simple, SPHINCS+-SHA256-256s-robust, SPHINCS+-SHA256-256s-simple
    - **SPHINCS+-SHAKE256**: SPHINCS+-SHAKE256-128f-robust, SPHINCS+-SHAKE256-128f-simple, SPHINCS+-SHAKE256-128s-robust, SPHINCS+-SHAKE256-128s-simple, SPHINCS+-SHAKE256-192f-robust, SPHINCS+-SHAKE256-192f-simple, SPHINCS+-SHAKE256-192s-robust, SPHINCS+-SHAKE256-192s-simple, SPHINCS+-SHAKE256-256f-robust, SPHINCS+-SHAKE256-256f-simple, SPHINCS+-SHAKE256-256s-robust, SPHINCS+-SHAKE256-256s-simple

liboqs does not support the following Round 3 alternate candidates: GeMSS.
