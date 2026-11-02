"""Check corpus identity and linkage; does not certify scientific conclusions."""
import csv
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
def read(name):
    with open(ROOT/'data'/name,newline='') as f:return list(csv.DictReader(f))
studies=read('included_studies.csv');library=read('reference_library.csv')
assert len(studies)==49, 'Technical corpus must contain 49 study records'
assert len(library)==89, 'Preserved source library must contain 89 records'
keys={x['key'] for x in studies}
assert len(keys)==49 and len({x['study_id'] for x in studies})==49, 'Duplicate study identity'
assert keys <= {x['key'] for x in library}, 'Unknown source-library citation key'
assert sum(x['role']=='technical inventory' for x in library)==49, 'Library role accounting differs'
for x in studies:
    assert x['title'] and x['year'] and x['labels'], 'Missing bibliographic/coding field'
    assert x['role'] in {'controller','adjacent','extension','evaluation'}, 'Unknown evidence role'
    assert urlparse(x['source_url']).scheme=='https', 'Missing primary source identifier'
for name in ['applied_audit.csv','protocol_audit.csv']:
    for x in read(name):assert x['citation_key'] in keys, 'Unresolved audit reference'
print('PASS: 49 unique studies, 89 library records, source identifiers and audit links')
