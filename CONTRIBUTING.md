# Contributing

Thank you for helping keep this list complete and correct.

## Adding a paper

1. Fork the repository and create a branch.
2. Add one row to the right section of `README.md` (and of the matching page under `pages/`) in this format:

   ```
   |[Title](Paper link)|Venue Year|[Code](Code link)|
   ```

3. If the paper reports results on a specific content type, add it to that type's page under `pages/content-types/`: one of the six content elements (running text, tables, figures and charts, equations, form fields, stamps and seals) or the two page-level properties (layout, typography).
4. Add the matching row to the CSV in `data/`.
5. Open a pull request that states the content type(s) and the benchmark the paper reports on.

## Inclusion criteria (paper Sec. 3.2)

A record is retained if it satisfies all four criteria:

- (C1) The retrieval corpus is a document collection and the retrieval unit is a page or page region, which excludes knowledge-based visual question answering over natural images.
- (C2) The work reports at least one quantitative result on a named benchmark, or contributes a benchmark, dataset or metric.
- (C3) The work is peer-reviewed, or is an archival preprint cited by at least one peer-reviewed work in the pool.
- (C4) Published in 2025-2026, or in the latest edition of a biennial venue. Foundational work cited to establish lineage is admitted without date restriction and is not counted in the pool.

## Corrections

Every field must trace to the original paper. If a link, venue or number is wrong, open an issue with the source.
