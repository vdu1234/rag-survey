# Stamps and seals

[← Form fields](form-fields.md) · [All content types](../../README.md#content-types) · [Layout →](layout.md)

<img src="../../images/content-types/stamps-and-seals.jpg" width="60%" alt="Stamps and seals: example region (paper Fig. 2)">

*Example region for stamps and seals, as shown around the hub in paper Fig. 2.* Stamps and seals is one of the six **content elements** (each occupies a region of the page) in the survey's content-type grouping (paper Sec. 2.2).

## Description (paper Sec. 2.2, word for word)

**Stamps and seals** mark authority, receipt or validity and are printed over other content by design. Work has separated overlaid marks from print [[85]](https://doi.org/10.1109/ICDAR.2011.236), surveyed seal-based retrieval [[29]](https://doi.org/10.1016/j.cosrev.2016.09.002), read the text inside 10,000 real seals [[43]](https://arxiv.org/pdf/2304.11966), erased seals [[86]](https://doi.org/10.1109/ICME55011.2023.00281) and checked them for forgery [[87]](https://doi.org/10.1109/ICSIP52628.2021.9688941), on a handful of datasets [[88]](https://doi.org/10.1007/978-3-319-68124-5_19), [[43]](https://arxiv.org/pdf/2304.11966), [[89]](https://doi.org/10.1007/s10032-026-00595-5); we found no retrieval system since 2020 that evaluates on them.

## Coverage in the content-type × paradigm matrix (paper Table 7)

|OCR → LLM|MLLM-native|Text RAG|Visual RAG|
|:-:|:-:|:-:|:-:|
|✗|✗|✗|✗|

✓ results reported; ○ the type has an established task but no method in that column reports on it; ✗ nothing reported.

## Benchmarks of paper Table 9 that annotate it

- [SPODS](https://doi.org/10.1007/978-3-319-68124-5_19) (ICVGIP-W 2017) · [link](https://facweb.iitkgp.ac.in/~jay/spods/index.html)
- [ReST](https://arxiv.org/pdf/2304.11966) (ICDAR 2023) · [link](https://arxiv.org/pdf/2304.11966)
- [DKDS](https://doi.org/10.1007/s10032-026-00595-5) (IJDAR 2026) · [link](https://ruiyangju.github.io/DKDS/pdf/paper.pdf)

## Benchmarks of paper Table 9 where it is present but not annotated

- none

## Works the paper cites for it

|No.|Paper|Venue|Year|
|--:|---|---|:-:|
|[85]|[Signature Segmentation from Machine Printed Documents Using Conditional Random Field](https://doi.org/10.1109/ICDAR.2011.236)|Proc. ICDAR|2011|
|[29]|[Logo and Seal Based Administrative Document Image Retrieval: A Survey](https://doi.org/10.1016/j.cosrev.2016.09.002)|Comput. Sci. Rev.|2016|
|[43]|[ICDAR 2023 Competition on Reading the Seal Title](https://arxiv.org/pdf/2304.11966)|Proc. ICDAR|2023|
|[86]|[Mask-Guided Stamp Erasure for Real Document Image](https://doi.org/10.1109/ICME55011.2023.00281)|Proc. ICME|2023|
|[87]|[Seal Imprint Verification Using SVM Classifier and Unmatched Key Point Features](https://doi.org/10.1109/ICSIP52628.2021.9688941)|Proc. ICSIP|2021|
|[88]|[SPODS: A Dataset of Color-Official Documents and Detection of Logo, Stamp, and Signature](https://doi.org/10.1007/978-3-319-68124-5_19)|Proc. ICVGIP Satellite Workshops|2017|
|[89]|[DKDS: A Benchmark Dataset of Degraded Kuzushiji Documents with Seals for Detection and Binarization](https://doi.org/10.1007/s10032-026-00595-5)|Int. J. Doc. Anal. Recognit.|2026|

[Back to README](../../README.md#content-types)
