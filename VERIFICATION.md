# Verification

Literature cut-off: **24 September 2026**. Every check below can be re-run with `python scripts/verify_repo.py` (add `--online` to open every GitHub link). [Back to README](README.md#verification)

This release follows the final version of the paper, **Visual Document Understanding with Retrieval-Augmented Generation: A Survey**. Every figure, table, number and reference below was compared with the paper source.

## Paper and repository

| Check | Result |
|---|---|
| Works cited in the paper | 232, each in [data/references.csv](data/references.csv) with `CitedInPaper = yes`; [data/vdu_rag.bib](data/vdu_rag.bib) is the paper's own bibliography file |
| Works collected but not cited (page limit) | 68, listed in [pages/further_reading.md](pages/further_reading.md) and Part B of the [master list PDF](supplementary/Master_List.pdf) |
| Reference numbers | [pages/paper_references.md](pages/paper_references.md) lists [1]-[232] exactly as numbered in the paper, then the works each of the 15 sections cites |
| Reference details | title, authors, year and venue of every reference are those of the paper's bibliography (including published versions: ColBERTv2 in NAACL 2022, RAGAs in EACL 2024, Chart-HQA in ACM MM 2025, MultiOCR-QA in CIKM 2025) |
| Methods (paper Tables 5-6) | 73, in the paper's order; name, venue, year (Findings marked), objective, index / unit and datasets equal to the paper tables ([pages/methods.md](pages/methods.md)) |
| Benchmarks (paper Table 9) | 25 key benchmarks, in the paper's order; venue, year, language, scope, size, queries, metric, the eight content-type marks and public flag equal to the paper table ([pages/datasets.md](pages/datasets.md)); 36 further benchmarks from 2025-2026 venues |
| EIOAR (paper Table 4) | 9 systems; encoder, index unit, operator, aggregator and reasoner equal to the paper table ([data/eioar.md](data/eioar.md)) |
| Scores (paper Table 8) | every value, footnote letter and note equal to the paper table ([pages/scores.md](pages/scores.md)) |
| Content-type × paradigm matrix (paper Table 7) | equal to the [content-type table](README.md#content-types) and to the matrix row on each [content-type page](pages/content-types/running-text.md) |
| Abstract and content-type descriptions | generated word for word from the paper source (abstract and Sec. 2.2), with the paper's citation numbers |
| Figures 1-11 and Tables 1-9 | rendered at 300 dpi from the paper source, with the paper's numbering, captions and citation numbers ([pages/figures_tables.md](pages/figures_tables.md)) |
| Fig. 1 values | works cited per year, 2020-2026: 5, 9, 15, 10, 24, 71, 73 (25 earlier works), equal to `data/references.csv` |
| Fig. 5 (PRISMA) values | 42 venue-year lists, 78,352 records, 101 arXiv duplicates (78,251 screened), 76,246 excluded, 2,014 related, 2,002 unique (9 arXiv duplicates of venue papers and 3 papers in both ICDAR and IJDAR 2026 counted once), 1,868 removed under (C1)-(C4), 134 cataloged (73 methods, 61 benchmarks), 232 cited, 88 earlier works; every count recomputed from `data/venues` by title match (case and punctuation ignored) |
| Sec. 3.1 arXiv split | of 543 arXiv records, 101 already in a venue list, 41 name a venue in the author comment, 401 preprints only; of the 65 related ones, 48 preprints only |
| Benchmarks cited only in the text | 21, listed with the sections that cite them in [pages/datasets.md](pages/datasets.md#3-other-benchmarks-and-datasets-cited-in-the-paper-21) |
| Wording | no page uses the earlier "channel" terminology or the removed channel-aware score; names follow the papers (ViDoRe V1/V2/V3, SERVAL, MIRACL-VISION, IRPAPERS) |

## Venue lists

| Check | Result |
|---|---|
| Records per venue-year | equal to [data/venues/index.csv](data/venues/index.csv) for all 42 lists |
| Duplicate titles within a venue-year | none |
| Related papers | every one is in its complete list |
| Link domain | matches the venue in every complete list (CVF, ACL Anthology, AAAI, OpenReview, PMLR, ECVA, IJCAI, JMLR, DOI, Springer) |
| Complete-list pages | 78,352 rows, every title clickable |
| Text encoding | no broken characters, LaTeX commands or HTML entities in any list or page (JMLR 2025/2026 author names and one ICML 2026 name repaired; the JMLR scraper now reads pages as UTF-8) |
| Markdown tables | all 275 tables have the same number of cells in every row |
| BMVC 2025, BMVC 2026, ICDAR 2026 | BMVC publishes no per-paper URL, and 119 of the 160 ICDAR 2026 papers had no Springer page at the cut-off; these titles open an arXiv title search, with a Google Scholar search beside them |

## Links

Every external link outside the venue lists (about 400 unique URLs in the README, `pages/`, `data/*.md` and `data/*.csv`) was opened one by one on 13-15 October 2026 and the page title compared with the reference.

| Check | Result |
|---|---|
| Relative links and section anchors in all Markdown files | all resolve |
| arXiv (108 papers; abs, pdf and html links) | all open, titles match |
| ACL Anthology (57 pages, plus 8 ACL DOIs) | all open, titles match |
| OpenReview (20 forum ids) | all match the paper's ICLR, NeurIPS or ICML page |
| CVF open access (20), ECVA (9), AAAI (6), PMLR (3), MLAnthology | all open, titles match; six CVPR 2026 pages are the URLs of the official CVF list |
| DOIs (82, plus 10 added in this check) | all resolve to the cited work (DOI resolver, OpenAlex, or the official SIGIR 2026, KDD 2026, ICDAR 2025, TPAMI and IJDAR lists) |
| GitHub code and project pages (52 repositories, 9 project pages, 4 Hugging Face pages) | all open |
| References without a stable open page | 1 (Nagy and Seth, ICPR 1984, which has no online page) opens a Google Scholar search, labelled `Scholar search` in [data/references.csv](data/references.csv); the other 20 earlier Scholar links now open the paper's DOI or official page |
| Venue-list pages (78,352 rows) | links are the hrefs of the official proceedings pages, checked for form and domain; a random paper from each of the 42 venue-years was opened on 13-15 October 2026 and every page that could be reached (AAAI, ACCV, ACL, EACL, EMNLP, CVPR, ICCV, ICCVW, WACV, ECCV, PMLR, arXiv, CVIU, TPAMI, IJDAR, IJCV, ICPR) showed the listed title |

Please open an [issue](.github/ISSUE_TEMPLATE/correction.md) for any link or value that is wrong.
