"""Apply frozen, visually checked additive source corrections; preserve old IDs.

Never rerun the legacy extractor over a published book to apply these corrections.
The unchanged source/pages.json and the frozen raw blocks retain provenance.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf8'))
def save(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf8')

book = read('public/data/book.json')
additions = read('source/additive-body.json')
support = read('source/structural-materials.json')
audit = read('source/source-audit-review.json')
assert book['pdfSha256'] == additions['pdfSha256'] == support['pdfSha256'] == audit['pdfSha256']
original = read('source/archive/reading-units-original-v1.json')
old_ids = {s for u in original for s in u['sentenceIds']}
before = [s for s in book['sentences'] if s['id'] in old_ids]
for addition in additions['additions']:
    for field, values in [('sections', [addition['section']]), ('paragraphs', [addition['paragraph']]), ('sentences', addition['sentences'])]:
        by_id = {x['id']: x for x in book[field]}
        for value in values:
            if value['id'] in by_id:
                assert by_id[value['id']] == value, ('Refuse source overwrite', value['id'])
            else:
                book[field].append(value)
    chapter = next(c for c in book['chapters'] if c['id'] == addition['section']['chapterId'])
    chapter['sectionIds'] = [addition['section']['id']] + [x for x in chapter['sectionIds'] if x != addition['section']['id']]
book['paragraphs'].sort(key=lambda p: (p['sources'][0]['pdfPage'], p['sources'][0]['block']))
positions = {p['id']: i for i, p in enumerate(book['paragraphs'])}
book['sentences'].sort(key=lambda s: (positions[s['paragraphId']], s['start']))
book['sections'].sort(key=lambda s: (s['chapterId'], s['number']))
assert [s for s in book['sentences'] if s['id'] in old_ids] == before
removed = {(s['pdfPage'], s['block']) for m in support['materials'] for s in m['sources']}
removed.update((a['paragraph']['sources'][0]['pdfPage'], a['paragraph']['sources'][0]['block']) for a in additions['additions'])
review_by_source = {(r['pdfPage'], r['block']): r for r in audit['records']}
book['excluded'] = [x for x in book['excluded'] if (x['pdfPage'], x.get('block')) not in removed]
for item in book['excluded']:
    review = review_by_source.get((item['pdfPage'], item.get('block')))
    if review:
        item['reason'] = review['reason']
book['supportMaterials'] = support['materials']
book['sourceAuditVersion'] = 1
save('public/data/book.json', book)
print('Applied additive source audit:', len(additions['additions']), 'body paragraphs;', len(support['materials']), 'support materials')
