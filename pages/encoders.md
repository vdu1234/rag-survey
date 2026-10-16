# What encoder families preserve and destroy (paper Table 3)

[Paper Table 3 (HD)](figures_tables.md#table-3) · [Fig. 4 (HD)](figures_tables.md#fig-4) · [Fig. 9 (HD)](figures_tables.md#fig-9) · [Back to README](../README.md#paper-to-repository-map)

|Family|Preserves|Destroys|
|---|---|---|
|**OCR → text**|reading text; word order within a block [[10]](https://doi.org/10.1109/ICDAR.2007.4376991), [[63]](https://arxiv.org/abs/2109.10282)|column order; table cell adjacency; anything non-textual [[134]](https://doi.org/10.1016/j.ipm.2025.104368), [[116]](https://aclanthology.org/2026.acl-industry.60/), [[135]](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html)|
|**Structured parsing**|text, layout, tables, formulas, reading order, each reported separately [[70]](https://arxiv.org/abs/2510.14528), [[68]](https://arxiv.org/abs/2512.02498)|typography; stamps; figures other than charts|
|**Layout-aware LM**|bounding boxes; reading order [[34]](https://arxiv.org/abs/1912.13318), [[133]](https://doi.org/10.18653/v1/2024.acl-long.463), [[92]](https://aclanthology.org/2025.findings-acl.379/)|typography; pixel content of figures and stamps|
|**Screenshot, single vector**|global page appearance [[22]](https://arxiv.org/abs/2406.11251), [[98]](https://openreview.net/forum?id=zG459X3Xge)|fine text; cell adjacency; anything below the pooled resolution|
|**Multi-vector visual**|patch-level appearance [[19]](https://openreview.net/forum?id=ogjBpZ8uSi)|content-type identity: matching follows appearance and position [[52]](https://doi.org/10.1145/3726302.3730285)|
|**Compressed visual**|whatever survives the pruning budget [[136]](https://ojs.aaai.org/index.php/AAAI/article/view/33076), [[110]](https://arxiv.org/abs/2509.23883)|*Unreported*: no work states which content types are dropped [[137]](https://aclanthology.org/2025.findings-acl.802/), [[138]](https://aclanthology.org/2026.acl-long.195/)|
|**Graph-structured**|relations the parser emitted [[91]](https://openreview.net/forum?id=Fu0aggezN9), [[69]](https://arxiv.org/abs/2506.05218)|relations it did not; the pixels behind every node|
|**Parse-informed multi-vector**|the *units* the parser returns [[139]](https://arxiv.org/abs/2603.01666), [[111]](https://doi.org/10.1007/978-3-032-36039-7_8)|a queryable type field: at most five coarse types, blended into the vectors [[111]](https://doi.org/10.1007/978-3-032-36039-7_8)|

“Unreported” marks a claim the literature does not make.

## Where the type label is lost (paper Sec. 5.3)

The table also shows where the type label is lost. A structured parser does assign content types, emitting a table as a table and a formula as a formula [[70]](https://arxiv.org/abs/2510.14528), [[69]](https://arxiv.org/abs/2506.05218). After that the label is dropped: chunking follows token count or layout, encoding keeps position and appearance (Eq. 2), the index stores a vector and an identifier, and late-interaction scoring sums over patches without knowing what they hold [[52]](https://doi.org/10.1145/3726302.3730285). No stage throws the label away on purpose; each has nowhere to put it. Two systems mark the edge of this claim. ColParse [[139]](https://arxiv.org/abs/2603.01666) embeds the regions a parser returns and fuses them with a page vector, so parser output reaches the index as a choice of *units*. LMS-Retrieval [[111]](https://doi.org/10.1007/978-3-032-36039-7_8) is the only surveyed retriever whose encoder takes a content-type label: its released code adds a learned embedding for five element types (text, title, equation, table, image) to every token vector of a parsed region. The label is blended into the vector rather than stored beside it, and stamps, form fields and typography stay unlabeled, yet it is the closest step we found toward type-aware retrieval. The screenshot position [[132]](https://aclanthology.org/2025.acl-long.943/) is therefore untested rather than refuted: no work we found tests it on the content types whose identity is hardest to recover from pixels (Sec. 9.2).

[Back to README](../README.md#paper-to-repository-map)
