# Separately dated revision discovery and method verification

Search date: 2 November 2026. Literature window: 1 January 2018–9 August 2026. This is supplementary discovery for a narrative review, not a recovered historical screening flow or an exhaustive systematic review.

PubMed returned 270 identifiers; arXiv returned 385 records. DOI/normalised-title matching removed five duplicates from 655 returns, leaving 650. A single AI-assisted title pass excluded 550 and advanced 100; abstract assessment classified 23 as outside the core scope, six as adjacent context and advanced 71 for method-focused verification. Crossref separately returned 1000 relevance-ranked records; its fuzzy total was never a screening denominator and the ranked sample is not included in the 650.

A method-focused, AI-assisted verification pass over the 71 advanced records found 44 with a supported runtime-control interface, eight adjacent methods or unestablished feedback boundaries, six contextual extensions/resources, one same-study version, two unresolved deployment-feedback descriptions, one unreconciled related version and nine records without an established full text. These are documentary assessment categories, not a new exhaustive included-study count or an independent quality rating. Unavailable or ambiguous records were not certified as feedback-driven controllers. The original 49-study reconstruction and the three purposive additions remain separately identified.

## Exact saved API parameters

### pubmed

```json
{
  "db": "pubmed",
  "term": "(agentic[Title/Abstract] OR \"reinforcement learning\"[Title/Abstract] OR \"multi-agent\"[Title/Abstract] OR \"intelligent agent\"[Title/Abstract] OR \"large language model\"[Title/Abstract] OR \"vision language model\"[Title/Abstract]) AND (restoration[Title/Abstract] OR reconstruction[Title/Abstract] OR denoising[Title/Abstract] OR \"super-resolution\"[Title/Abstract] OR \"image enhancement\"[Title/Abstract] OR \"artifact correction\"[Title/Abstract] OR \"MRI sampling\"[Title/Abstract]) AND (\"2018/01/01\"[Date - Publication] : \"2026/08/09\"[Date - Publication])",
  "retmode": "json",
  "retmax": 10000
}
```

### arxiv

```json
{
  "search_query": "(all:agentic OR all:\"reinforcement learning\" OR all:\"multi-agent\" OR all:\"intelligent agent\" OR all:\"LLM agent\" OR all:\"VLM agent\") AND (ti:restoration OR ti:reconstruction OR ti:denoising OR ti:\"super-resolution\" OR ti:\"image enhancement\" OR ti:\"artifact correction\") AND submittedDate:[201801010000 TO 202608092359]",
  "start": 0,
  "max_results": 2000,
  "sortBy": "submittedDate",
  "sortOrder": "ascending"
}
```

### crossref

```json
{
  "query.bibliographic": "agentic image restoration reconstruction reinforcement learning",
  "filter": "from-pub-date:2018-01-01,until-pub-date:2026-08-09",
  "rows": 1000
}
```

## Files and interpretation

`data/revision_search_screening.csv` supplies metadata and the recorded decisions/reasons. Full abstracts and article text are not redistributed here. `data/method_assessment.csv` supplies the 71 method-focused dispositions with primary identifiers and evidence basis. `data/included_studies.csv` is the 52-study purposive synthesis inventory, not all records considered eligible in discovery. Some literature-supported runtime-control records are outside this review's selected representative examples.

One AI-assisted assessment is not independent dual-human screening. Source-version, reporting and applicability judgments remain limited by the available texts. The public records support inspection of what was done; they do not establish complete recall of AIR literature.
