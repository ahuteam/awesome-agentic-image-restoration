"""Check corpus identity and linkage; does not certify scientific conclusions."""
import csv
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
print('PASS: 52 unique studies, 92 library records, source identifiers and audit links')
