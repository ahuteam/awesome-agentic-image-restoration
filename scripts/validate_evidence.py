"""Check corpus identity and linkage; does not certify scientific conclusions."""
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
def read(name):
    with open(ROOT/'data'/name,newline='') as f:return list(csv.DictReader(f))
studies=read('included_studies.csv');library=read('reference_library.csv')
assert len(studies)==52, 'Technical corpus must contain 52 study records'
assert len(library)==92, 'Preserved source library must contain 92 records'
keys={x['key'] for x in studies}
assert len(keys)==52 and len({x['study_id'] for x in studies})==52, 'Duplicate study identity'
assert {x['key'] for x in studies if x['study_id'] in {'AIR50','AIR51','AIR52'}} == {'chen2024starrl','jia2026tiragent','zhuang2026evoir'}, 'Revision additions lost or reassigned'
assert keys <= {x['key'] for x in library}, 'Unknown source-library citation key'
assert sum(x['role']=='technical inventory' for x in library)==52, 'Library role accounting differs'
for x in studies:
    assert x['title'] and x['year'] and x['labels'], 'Missing bibliographic/coding field'
    assert x['role'] in {'controller','adjacent','extension','evaluation'}, 'Unknown evidence role'
    assert urlparse(x['source_url']).scheme=='https', 'Missing primary source identifier'
for name in ['applied_audit.csv','protocol_audit.csv']:
    for x in read(name):assert x['citation_key'] in keys, 'Unresolved audit reference'
screen=read('revision_search_screening.csv');method=read('method_assessment.csv')
assert len(screen)==655 and len({x['record_id'] for x in screen})==655, 'Raw discovery identity mismatch'
assert Counter(x['title_decision'] for x in screen)=={'duplicate':5,'exclude_at_title':550,'advance':100}, 'Raw/deduplicated/title counts differ'
all_ids={x['record_id'] for x in screen}
assert all(x['duplicate_of'] in all_ids for x in screen if x['title_decision']=='duplicate'), 'Duplicate target does not resolve'
advanced=[x for x in screen if x['title_decision']=='advance']
assert len(advanced)==100, 'Title-stage denominator mismatch'
assert Counter(x['abstract_decision'] for x in advanced)=={'exclude':23,'adjacent_context':6,'advance_to_full_text':71}, 'Abstract-stage counts differ'
assert {x['record_id'] for x in method}=={x['record_id'] for x in advanced if x['abstract_decision']=='advance_to_full_text'}, 'Method assessment does not cover the advanced records'
expected=json.loads((ROOT/'data/method_assessment_counts.json').read_text())
assert Counter(x['assessment'] for x in method)==expected, 'Method disposition counts differ'
assert all(x['basis'] and x['primary_identifier'] for x in method), 'Method disposition lacks a source or reason'
print('PASS: 52 studies, 92 library entries, linked audits and 655 raw records / 650 deduplicated records in the revision ledger')
