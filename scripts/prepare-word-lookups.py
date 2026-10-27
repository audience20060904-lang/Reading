"""Compile selected, prewritten lexical notes at exact source occurrences.

This script does not infer word senses. Context glosses come from existing authored
vocabulary or explicitly authored overrides. It never changes the book/questions.
"""
from pathlib import Path
import hashlib,json,re
import subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
if (ROOT/'source/b2-vocabulary/author-notes.json').exists():
 subprocess.run(['node','scripts/compile-b2-lookups.mjs'],cwd=ROOT,check=True)
 sys.exit(0)
read=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
book=read('public/data/book.json');questions=read('public/data/questions.json')
paragraphs={p['id']:p for p in book['paragraphs']};sentences={s['id']:s for s in book['sentences']}
entries={};forms={}
for line in (ROOT/'source/word-lexicon.tsv').read_text(encoding='utf8').splitlines():
 if not line.strip() or line.startswith('#'):continue
 headword,matches,kind,other=line.split('|')
 entry_id=headword.lower().replace(' ','-')
 assert entry_id not in entries and kind in ('difficult','shifted')
 entries[entry_id]=dict(id=entry_id,headword=headword,kind=kind,otherMeanings=other.split(';') if other else [])
 for form in matches.split(','):
  assert form.lower() not in forms
  forms[form.lower()]=entry_id

occurrences={}
def add(paragraph,start,end,entry_id,meaning,origin):
 assert start>=0 and end>start and end<=len(paragraph['text'])
 assert not re.search(r'正确答案|选项|答案为',meaning)
 key=f"{paragraph['id']}@{start}:{end}"
 value=dict(id=key,paragraphId=paragraph['id'],start=start,end=end,text=paragraph['text'][start:end],entryId=entry_id,contextMeaning=meaning,sentenceIds=[sid for sid in paragraph['sentenceIds'] if sentences[sid]['start']<end and sentences[sid]['end']>start])
 if key in occurrences:
  assert occurrences[key]['entryId']==entry_id
  return
 occurrences[key]=value

for q in questions:
 p=paragraphs[q['paragraphId']];offset=p['text'].find(q['passage']);assert offset>=0
 for v in q['vocabulary']:
  entry_id=forms.get(v['word'].lower())
  if not entry_id:continue
  for match in re.finditer(r'(?<![A-Za-z])'+re.escape(v['word'])+r'(?![A-Za-z])',q['passage'],re.I):
   add(p,offset+match.start(),offset+match.end(),entry_id,v['meaning'],q['id'])

# The first sentence contains a concrete difficult noun absent from its exercise's
# vocabulary list. Its lexical gloss is authored here, not guessed at runtime.
first=book['sentences'][0];p=paragraphs[first['paragraphId']];surface='clementines';start=p['text'].index(surface)
add(p,start,start+len(surface),'clementine','小柑橘；这里指九州当地的一种柑橘类物产。','first-body-sentence')

ordered=sorted(occurrences.values(),key=lambda o:(next(i for i,p in enumerate(book['paragraphs']) if p['id']==o['paragraphId']),o['start']))
by_paragraph={}
for item in ordered:
 group=by_paragraph.setdefault(item['paragraphId'],[])
 assert not group or group[-1]['end']<=item['start'],'Resolve overlapping lexical selections explicitly'
 group.append(item)
used={o['entryId'] for o in ordered}
catalog=dict(version=1,pdfSha256=book['pdfSha256'],selection='Selected difficult words and context-specific familiar words/phrases only; not a complete dictionary or CEFR classification.',entries=[e for k,e in entries.items() if k in used],paragraphs=by_paragraph)
target=ROOT/'src/data/word-lookups.json';content=json.dumps(catalog,ensure_ascii=False,indent=2)+'\n'
if not target.exists() or target.read_text(encoding='utf8')!=content:target.write_text(content,encoding='utf8')
report=dict(version=1,date='2026-10-25',pdfSha256=book['pdfSha256'],entryCount=len(used),occurrenceCount=len(ordered),paragraphCount=len(by_paragraph),byChapter={c['id']:sum(paragraphs[o['paragraphId']]['chapterId']==c['id'] for o in ordered) for c in book['chapters']},sources=['source/word-lexicon.tsv','public/data/questions.json: vocabulary.meaning','public/data/book.json: original offsets'],rules=['Only selected exact occurrences are blue; ordinary words are not made clickable.','Context glosses are prewritten lexical meanings, never question answers, analyses or full passage translations.','Other common senses are authored lexical notes; monosemous entries explicitly have no additional common sense.','No runtime AI, network dictionary, stemming or sense guessing.','Source text, question objects, fingerprints and personal study data are not modified.'],unmatchedDraftEntries=[k for k in entries if k not in used])
(ROOT/'source/word-lookup-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:report[k] for k in ['entryCount','occurrenceCount','paragraphCount','byChapter']},ensure_ascii=False))
