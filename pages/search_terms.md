# Search and screening terms (paper Table 2)

[Paper Table 2 (HD)](figures_tables.md#table-2) · [Fig. 5 PRISMA (HD)](figures_tables.md#fig-5) · [Back to README](../README.md#paper-to-repository-map)

*Search and Screening Terms. Venue-year lists were retrieved in full, not by query; groups D, R and E only flag records for manual reading (a record is flagged if its title or abstract matches any term, D OR R OR E). arXiv was queried directly with the phrase groups A<sub>1</sub>–A<sub>5</sub>.*

|Group|Terms (title and abstract, case-insensitive)|
|---|---|
|*D* (document)|visually rich, document, DocVQA, multi-page, PDF, OCR, layout, chart, infographic, slide, screenshot, text-rich, scanned, table understanding / question / recognition / structure, handwriting, scene text, formula, key information, information extraction|
|*R* (retrieval)|retrieval-augmented, RAG (incl. \*RAG, GraphRAG), ColPali, ColQwen, late interaction, multi-vector, multimodal retrieval, visual retrieval, document retrieval|
|*E* (efficiency)|visual token, token pruning / compression / reduction, high-resolution|
|Dataset flag|title: dataset, benchmark, corpus, \*Bench; abstract: we introduce / present / propose / release / construct / curate … dataset / benchmark / corpus|
|Excluded matches|whole-slide (pathology), tabular machine learning, lookup tables, drag, storage, leverage (substring false positives)|
|**arXiv group**|**Phrases (title OR abstract)**|
|A<sub>1</sub>–A<sub>5</sub>|five phrase groups: A<sub>1</sub> visual document RAG (e.g., “visual document retrieval”, “visual RAG”, ColPali, ViDoRe); A<sub>2</sub> VDU and document QA (e.g., “visually rich document”, DocVQA, “multi-page document”); A<sub>3</sub> parsing (e.g., “document layout analysis”, “table structure recognition”); A<sub>4</sub> charts, tables and slides (e.g., “chart question answering”, infographic); A<sub>5</sub> multi-vector retrieval (e.g., “late interaction retrieval”). The complete phrase lists are in the project's arXiv collection script.|
|arXiv filter|each A<sub>i</sub> AND categories cs.CV, cs.CL, cs.IR, cs.AI, cs.LG or cs.MM AND submitted in 2026 up to the cut-off; all five result lists read to the end (Sec. 3.1)|

The arXiv collection script with the complete phrase lists is [`scripts/arxiv_scraper.py`](../scripts/arxiv_scraper.py).

[Back to README](../README.md#paper-to-repository-map)
