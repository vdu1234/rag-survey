# Checklist: designing and reporting a VDU-RAG system (paper Fig. 11)

[Paper Fig. 11 (HD)](figures_tables.md#fig-11) · [Back to README](../README.md#paper-to-repository-map)

## Design (paper Secs. 10 and 6)

- [ ] Which content types do the queries need? Parse for text, tables, formulas and reading order; use pixels for stamps, typography and non-chart figures.
- [ ] How large is the corpus? Tens of pages: place them in context; thousands: retrieve.
- [ ] What should be returned? Choose page, region or element per query.
- [ ] What index size is affordable? Multi-vector costs about v times a single vector.
- [ ] Is the script covered by the retriever's training data?
- [ ] Can each answer show its evidence? Return an evidence box with it.

## Report (18 items, paper Sec. 9.3)

|Group|Items|
|---|---|
|**R** *Retrieval*|backbone and size; depth K; index type; page resolution.|
|**P** *Parsing*|parser and version; structure used or characters only; chunking.|
|**E** *Evaluation*|metric implementation; benchmark version; split; runs; variance.|
|**C** *Corpus*|source and license; size in pages; content-type composition.|
|**A** *Availability*|code; weights; license on both.|

## Evaluate (paper Sec. 11)

Report retrieval metrics per content type of the evidence (Sec. 11) alongside page-level nDCG.

## What the evidence already supports (paper Sec. 14)

Before turning to what remains open, we distill what the evidence already supports. Parse running text and layout, since with a textual re-ranker a parsed pipeline retrieved best on ViDoRe V3 [[113]](https://aclanthology.org/2026.acl-long.755/); use a chart-aware parser [[70]](https://arxiv.org/abs/2510.14528), [[75]](https://arxiv.org/abs/2404.09987) or pixels for charts, and pixels for other figures; treat tables as mixed evidence and stamps and typography as untested; skip retrieval for small corpora; and run both pipelines when they disagree, since combining their top pages answers hard questions best [[113]](https://aclanthology.org/2026.acl-long.755/) and reconciling the two paths helps multi-document QA [[106]](https://arxiv.org/abs/2412.10704).

[Back to README](../README.md#paper-to-repository-map)
