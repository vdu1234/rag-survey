"""Rebuild pages/scores.md and data/scores.md: paper Table 8 as printed, then every value with its source table."""
import pandas as pd
ref=pd.read_csv('data/references.csv'); L=dict(zip(ref.BibKey,ref.Link))
s=pd.read_csv('data/scores.csv',dtype=str,keep_default_na=False)
def P(k,n): return f'[{n}]({L[k]})'
ret=[('ColPali','fayssecolpali2025','PaliGemma-3B','81.3','n/r','n/r','[code](https://github.com/illuin-tech/colpali)'),
('ColMate','masry2025colmate','ColPali-3B','85.14','57.61 (a)','n/r','[link](https://arxiv.org/pdf/2511.00903)'),
('ColModernVBERT','teiletche2025modernvbert','0.25B','81.2','56.0 (b)','n/r','[code](https://huggingface.co/ModernVBERT)'),
('VLM2Vec-V2','meng2025vlm2vecv2','','75.5 (c)','44.9 (c)','n/r','[code](https://tiger-ai-lab.github.io/VLM2Vec/)'),
('ColParse','beyondgrid2026','GME-7B','89.56','62.12 (d)','n/r','[link](https://arxiv.org/pdf/2603.01666)'),
('LightSTAR','lightstar2026eccv','2B','89.1 (e)','n/r','n/r','[code](https://github.com/bokufa/LightSTAR)'),
('MetaEmbed','xiaometaembed2026','7B / 3B','n/r','61.3 / 60.3 (f)','n/r','[code](https://github.com/facebookresearch/MetaEmbed)'),
('Evo-Retriever','evoretriever2026cvpr','7B / 3B','n/r','65.2 / 63.3 (d)','n/r','[link](https://arxiv.org/pdf/2603.16455)'),
('AGREE','agree2026sigir','Qwen2.5-VL','n/r','61.54 (d)','n/r','[link](https://arxiv.org/pdf/2511.13415)'),
('SERVAL','nguyen2025serval','Qwen2.5-VL-32B','n/r','63.4 (g)','n/r','[code](https://github.com/thongnt99/serval)'),
('AGC','mvcompress2026sigir','64 tokens','n/r','56.7 (h)','n/r','[code](https://github.com/hanxiangqin/omni-col-press)'),
('Nemotron ColEmbed V2','moreira2026nemotroncolembed','8B','n/r','n/r','63.42','[link](https://arxiv.org/pdf/2602.03992)')]
e2e=[('SV-RAG','chensvrag2025','InternVL2','23.0','n/r','[link](https://arxiv.org/pdf/2411.01106)'),
('MDocAgent','han2025mdocagent','best setting','31.5','57.8','[link](https://arxiv.org/pdf/2503.13964)'),
('CMRAG','cmrag2025','top-3','31.05','48.18 (i)','[code](https://github.com/WangWarrenChen/CMRAG)'),
('ALDEN','alden2026acl','Qwen2.5-VL-7B','38.5 (j)','54.2 (j)','[link](https://arxiv.org/pdf/2510.25668)'),
('Doc-V*','docvstar2026acl','Qwen2.5-VL-7B','42.1','56.3','[code](https://github.com/SeerRay-Lab/Doc-V)'),
('LAD-RAG','sourati-etal-2026-lad','InternVL2-8B','44.8','47.7','[link](https://arxiv.org/pdf/2510.07233)'),
('MM-Doc-R1','mmdocr12026acl','Qwen3-8B','49.7','n/r','[link](https://arxiv.org/pdf/2604.13579)'),
('URaG','urag2026aaai','7B','n/r','52.2','[code](https://github.com/shi-yx/URaG)'),
('MARDoc','chen2026mardoc','Qwen3-VL-30B','57.1','n/r','[link](https://arxiv.org/pdf/2606.05749)'),
('MARDoc','chen2026mardoc','Qwen3-VL-8B','52.7','n/r','[link](https://arxiv.org/pdf/2606.05749)'),
('DocLens','zhu2025doclens','Gemini-2.5-Pro','67.6','n/r','[code](https://dwzhu-pku.github.io/DocLens/)')]
o=['# Reported scores (paper Table 8)','','[Paper Table 8 (HD)](figures_tables.md#table-8) · [Fig. 8 (HD)](figures_tables.md#fig-8)','','[Back to README](../README.md#metrics-and-reported-scores) · [Metrics](metrics.md) · [Raw file](../data/scores.csv)','',
'Scores as reported by each paper for itself, copied from its own result table and not re-run or rescaled. ViDoRe V2 averages cover different subsets across papers (letters), so V2 values compare only within a letter. In the end-to-end part the reader model differs by row and dominates the score. n/r = not reported; a blank cell = not stated by the paper (as in paper Table 8).','',
'## Retrieval (nDCG@5; ViDoRe V3: nDCG@10)','','|Retriever|Backbone|ViDoRe V1|ViDoRe V2|ViDoRe V3|Link in paper|','|---|---|:-:|:-:|:-:|:-:|']
o+=[f'|{P(k,n)}|{b}|{v1}|{v2}|{v3}|{l}|' for n,k,b,v1,v2,v3,l in ret]
o+=['','## End-to-end accuracy (%)','','|Pipeline|Reader|MMLongBench-Doc|LongDocURL|Link in paper|','|---|---|:-:|:-:|:-:|']
o+=[f'|{P(k,n)}|{r}|{a}|{b}|{l or "-"}|' for n,k,r,a,b,l in e2e]
o+=['','ViDoRe V2 subsets: (a) nine incl. multilingual; (b) English; (c) MMEB-V2 protocol; (d) four English; (f) seven; (g) nine, zero-shot; (h) multilingual. (e) eight of the ten V1 subsets. (i) filtered subset. (j) hybrid text and visual retrieval.','',
'**Also reported** (paper Table 8 notes): ColParse ViDoSeek 84.12; HEAVEN ViDoSeek R@1 75.04; ReAlign 80.0 avg. nDCG@5 on six benchmarks (Qwen backbone); VisDoMRAG 44.11 / 63.28 / 67.22 on PaperTab / FetaTab / SlideVQA; HKRAG SlideVQA 56.5, DUDE 45.2; SlideAgent SlideVQA 84.9 (GPT-4o); SCoPE VLM MMLongBench-Doc ANLS 17.90.','',
'**Relative gains reported over each paper\'s own baselines**: '+P('ma2024dse','DSE')+' +17 points top-1 over BM25 on Wiki-SS; '+P('yuvisrag2025','VisRAG')+' 20-40% end-to-end over text-based RAG; '+P('suri2025visdom','VisDoMRAG')+' 12-20% on VisDoMBench; '+P('wang-etal-2025-vidorag','ViDoRAG')+' over 10% on ViDoSeek; '+P('han2025mdocagent','MDocAgent')+' +12.1% on average over five benchmarks; '+P('liregionrag2026','RegionRAG')+' +10.02% R@1 and +3.56% accuracy with 71.42% of the visual tokens.','',
'## Every value with its source table','','|Method|Paper|Values as reported|Source table|','|---|---|---|---|']
o+=[f'|{x.Method}|{P(x.Key,"paper") if x.Key in L else ""}|{x.Values}|{x.iloc[2]}|' for _,x in s.iterrows()]
open('pages/scores.md','w',encoding='utf-8').write('\n'.join(o)+'\n')
open('data/scores.md','w',encoding='utf-8').write('\n'.join(o).replace('(../README.md','(../README.md').replace('](metrics.md)','](../pages/metrics.md)').replace('](figures_tables.md','](../pages/figures_tables.md').replace('](../data/scores.csv)','](scores.csv)')+'\n')
print('ok')
