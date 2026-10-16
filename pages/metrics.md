# Metrics

[Back to README](../README.md#metrics-and-reported-scores) · [Scores](scores.md) · [Datasets](datasets.md) · [Paper Table 9 (HD)](figures_tables.md#table-9)

## Metrics of the key benchmarks (paper Table 9)

Every metric that appears in the Metric column of paper Table 9, with the benchmarks that use it.

|Metric|What it measures|Used by|
|---|---|---|
|nDCG@5|Normalized discounted cumulative gain over the top 5 pages|ViDoRe V1, ViDoRe V2, ViDoSeek|
|R@5|Recall at 5|ViDoRe V2, ViDoRe V3, ViDoSeek|
|nDCG@10|Normalized discounted cumulative gain over the top 10 pages|ViDoRe V3|
|R@1|Recall at 1|ViDoRe V3, ViDoSeek|
|mAP|Mean average precision|ViDoRe V3, MMDocIR, DocLayNet|
|nDCG@1/3/5|nDCG at cut-off 1, 3 and 5|MMDocIR|
|R@1/3/5|Recall at 1, 3 and 5|MMDocIR|
|BLEU|n-gram overlap of the generated answer|MMDocRAG, SPIQA|
|ROUGE-L|Longest-common-subsequence overlap of the generated answer|MMDocRAG|
|ANLS|Average normalized Levenshtein similarity (introduced with ST-VQA)|M3DocVQA, DocVQA, InfographicVQA, MTVQA|
|F1|Harmonic mean of precision and recall|M3DocVQA, SciEGQA, TAT-DQA, FUNSD, VRDU, SPODS, ReST, DKDS, TexTAR|
|P@10|Precision at 10|UniDoc-Bench|
|R@10|Recall at 10|UniDoc-Bench|
|relaxed acc.|Numeric answers correct within a small relative tolerance|ChartQA|
|EM|Exact match with the gold answer|TAT-DQA|
|ROUGE|n-gram recall overlap of the generated answer|SPIQA|
|BERTScore|Embedding similarity of generated and gold answers|SPIQA|
|L3Score|LLM-judged answer score|SPIQA|
|Accuracy|Share of answers judged correct|LongDocURL, MTVQA, ReST|
|AP|Average precision of detected tables|PubTables-1M|
|GriTS|Grid table similarity of predicted and gold cell grids|PubTables-1M|
|CDM|Character detection matching for formula recognition|UniMER|
|P|Precision|TexTAR|
|R|Recall|TexTAR|

## Metrics and their blind spots (paper Sec. 11, word for word)

**Evaluation metrics.** Metrics follow the subtasks. *Retrieval* is scored with Recall@k, mean reciprocal rank and, above all, nDCG@k [[219]](https://doi.org/10.1145/582415.582418), the primary metric of the ViDoRe family. *Answering* is scored with ANLS [[220]](https://arxiv.org/abs/1905.13648), the standard DocVQA metric, which forgives small string differences below a threshold of 0.5; with exact match and token-level F1 for extraction; and with relaxed accuracy, a 5% numeric tolerance, for ChartQA [[40]](https://arxiv.org/abs/2203.10244). *Structure* is scored with mAP for layout [[16]](https://arxiv.org/abs/1908.07836) and grid-similarity scores for tables [[15]](https://arxiv.org/abs/2110.00061). End-to-end RAG adds automatic faithfulness metrics [[221]](https://aclanthology.org/2024.eacl-demo.16/), designed for text.

Each metric is blind in its own way: nDCG scores the *page*, ANLS the *string*, and neither says which content was responsible for a hit. This already changes conclusions: two formula metrics order the same pair of systems in opposite directions [[120]](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Image_Over_Text_Transforming_Formula_Recognition_Evaluation_with_Character_Detection_CVPR_2025_paper.html), relevance labels correlate only weakly with downstream utility [[222]](https://doi.org/10.1145/3626772.3657957), and the evaluation of multimodal RAG is itself contested [[223]](https://arxiv.org/abs/2508.03644). This answers (Q4): page-level relevance is the wrong unit, not only because it is coarse but because a better page score need not mean better answers.

A first remedy needs no new metric: report standard retrieval metrics separately by the content type of the evidence. The evidence boxes of ViDoRe V3 already carry such a label (text, table, chart, infographic, image, mixed or other) [[113]](https://aclanthology.org/2026.acl-long.755/), and structured parsers emit the same element types [[70]](https://arxiv.org/abs/2510.14528); stamps and typography, however, are annotated by no retrieval benchmark we found.


[Back to README](../README.md#metrics-and-reported-scores)
