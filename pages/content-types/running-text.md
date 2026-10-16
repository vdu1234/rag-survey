# Running text

[All content types](../../README.md#content-types) · [Tables →](tables.md)

<img src="../../images/content-types/running-text.jpg" width="60%" alt="Running text: example region (paper Fig. 2)">

*Example region for running text, as shown around the hub in paper Fig. 2.* Running text is one of the six **content elements** (each occupies a region of the page) in the survey's content-type grouping (paper Sec. 2.2).

## Description (paper Sec. 2.2, word for word)

**Running text** is the characters and their reading order; because order belongs to the layout, perfect character accuracy can still yield an unreadable stream. Text is recognized by engineered recognizers [[10]](https://doi.org/10.1109/ICDAR.2007.4376991), sequence models [[63]](https://arxiv.org/abs/2109.10282), OCR-free generators [[64]](https://arxiv.org/abs/2111.15664), [[65]](https://arxiv.org/abs/2203.16618), [[66]](https://arxiv.org/abs/2304.12484), and compact vision-language models that emit markdown, layout and reading order together [[67]](https://doi.org/10.1109/tpami.2026.3653415), [[68]](https://arxiv.org/abs/2512.02498), [[69]](https://arxiv.org/abs/2506.05218), [[70]](https://arxiv.org/abs/2510.14528).

## Coverage in the content-type × paradigm matrix (paper Table 7)

|OCR → LLM|MLLM-native|Text RAG|Visual RAG|
|:-:|:-:|:-:|:-:|
|✓|✓|✓|✓|

✓ results reported; ○ the type has an established task but no method in that column reports on it; ✗ nothing reported.

## Benchmarks of paper Table 9 that annotate it

- [ViDoRe V1](https://openreview.net/forum?id=ogjBpZ8uSi) (ICLR 2025) · [link](https://arxiv.org/pdf/2407.01449)
- [ViDoRe V2](https://arxiv.org/abs/2505.17166) (arXiv 2025) · [link](https://arxiv.org/pdf/2505.17166)
- [ViDoRe V3](https://aclanthology.org/2026.acl-long.755/) (ACL 2026) · [link](https://arxiv.org/pdf/2601.08620)
- [MMDocIR](https://aclanthology.org/2025.emnlp-main.1576/) (EMNLP 2025) · [link](https://huggingface.co/MMDocIR)
- [MMDocRAG](https://papers.nips.cc/paper_files/paper/2025/hash/1a93178950e92fd2e7b7448f7d68fd7d-Abstract-Datasets_and_Benchmarks_Track.html) (NeurIPS 2025) · [link](https://github.com/MMDocRAG/MMDocRAG)
- [M3DocVQA](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html) (ICCVW 2025) · [link](https://github.com/bloomberg/m3docrag)
- [ViDoSeek](https://aclanthology.org/2025.emnlp-main.464/) (EMNLP 2025) · [link](https://github.com/Alibaba-NLP/ViDoRAG)
- [UniDoc-Bench](https://arxiv.org/abs/2510.03663) (arXiv 2025) · [link](https://github.com/SalesforceAIResearch/UniDOC-Bench)
- [SciEGQA](https://yuwenhan07.github.io/SciEGQA-project/) (arXiv 2026) · [link](https://yuwenhan07.github.io/SciEGQA-project/)
- [DocVQA](https://doi.org/10.1109/WACV48630.2021.00225) (WACV 2021) · [link](https://arxiv.org/pdf/2007.00398)
- [InfographicVQA](https://arxiv.org/abs/2104.12756) (WACV 2022) · [link](https://arxiv.org/pdf/2104.12756)
- [TAT-DQA](https://arxiv.org/abs/2207.11871) (ACM MM 2022) · [link](https://github.com/NExTplusplus/TAT-DQA)
- [SPIQA](https://arxiv.org/abs/2407.09413) (NeurIPS 2024) · [link](https://arxiv.org/pdf/2407.09413)
- [LongDocURL](https://aclanthology.org/2025.acl-long.57/) (ACL 2025) · [link](https://github.com/dengc2023/LongDocURL)
- [MTVQA](https://aclanthology.org/2025.findings-acl.404/) (ACL Find. 2025) · [link](https://github.com/bytedance/MTVQA)
- [FUNSD](https://arxiv.org/abs/1905.13538) (ICDARW 2019) · [link](https://guillaumejaume.github.io/FUNSD/)
- [VRDU](https://doi.org/10.1145/3580305.3599929) (KDD 2023) · [link](https://github.com/google-research-datasets/vrdu)
- [DocLayNet](https://doi.org/10.1145/3534678.3539043) (KDD 2022) · [link](https://github.com/DS4SD/DocLayNet)
- [TexTAR](https://doi.org/10.1007/978-3-032-04614-7_16) (ICDAR 2025) · [link](https://arxiv.org/pdf/2509.13151)

## Benchmarks of paper Table 9 where it is present but not annotated

- [ChartQA](https://arxiv.org/abs/2203.10244) (ACL Find. 2022)
- [PubTables-1M](https://arxiv.org/abs/2110.00061) (CVPR 2022)
- [UniMER](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_UniMERNet_A_Universal_Network_for_Real-World_Mathematical_Expression_Recognition_CVPR_2026_paper.html) (CVPR 2026)
- [SPODS](https://doi.org/10.1007/978-3-319-68124-5_19) (ICVGIP-W 2017)
- [ReST](https://arxiv.org/pdf/2304.11966) (ICDAR 2023)
- [DKDS](https://doi.org/10.1007/s10032-026-00595-5) (IJDAR 2026)

## Works the paper cites for it

|No.|Paper|Venue|Year|
|--:|---|---|:-:|
|[10]|[An Overview of the Tesseract OCR Engine](https://doi.org/10.1109/ICDAR.2007.4376991)|Proc. ICDAR|2007|
|[63]|[TrOCR: Transformer-Based Optical Character Recognition with Pre-trained Models](https://arxiv.org/abs/2109.10282)|Proc. AAAI|2023|
|[64]|[OCR-free Document Understanding Transformer](https://arxiv.org/abs/2111.15664)|Proc. ECCV|2022|
|[65]|[End-to-End Document Recognition and Understanding with Dessurt](https://arxiv.org/abs/2203.16618)|Proc. ECCV Workshops|2022|
|[66]|[DocParser: End-to-End OCR-free Information Extraction from Visually Rich Documents](https://arxiv.org/abs/2304.12484)|Proc. ICDAR|2023|
|[67]|[TextMonkey: An OCR-free Large Multimodal Model for Understanding Document](https://doi.org/10.1109/tpami.2026.3653415)|IEEE Trans. Pattern Anal. Mach. Intell.|2026|
|[68]|[dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model](https://arxiv.org/abs/2512.02498)|arXiv preprint arXiv:2512.02498|2025|
|[69]|[MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm](https://arxiv.org/abs/2506.05218)|arXiv preprint arXiv:2506.05218|2025|
|[70]|[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://arxiv.org/abs/2510.14528)|arXiv preprint arXiv:2510.14528|2025|

[Back to README](../../README.md#content-types)
