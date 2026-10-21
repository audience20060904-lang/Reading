"""Build a lossless, non-overlapping reading plan and explicitly edited v2 exercises.
Never creates questions for unprepared text. Every original candidate sentence occurs once.
"""
from pathlib import Path
import json,hashlib,re,runpy,copy
ROOT=Path(__file__).resolve().parents[1]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
def save(p,v):
 path=ROOT/p;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
b=load('public/data/book.json');assert b['pdfSha256']=='be25c859f1bd894a4b0d1cff024ded1297f6a96a8e8ddabea1e3abcf89160a50'
archive=ROOT/'source/archive/questions-v1.json'
if not archive.exists():
 old=load('public/data/questions.json');assert all(q['version']==1 for q in old);save('source/archive/questions-v1.json',old)
old=load('source/archive/questions-v1.json');R=runpy.run_path(str(ROOT/'scripts/batches/short-passages.py'))['R']
assert {q['id'] for q in old}==set(R),'Each new question needs an explicitly reviewed short range'
ss=b['sentences'];paragraphs={p['id']:p for p in b['paragraphs']};byid={s['id']:s for s in ss};position={s['id']:i for i,s in enumerate(ss)}
words=lambda t:len(re.findall(r'\S+',t))
def vocab(word,meaning,context,example,*collocations):return dict(word=word,meaning=meaning,context=context,example=example,collocations=list(collocations))
extra={
'q-c01-013':vocab('maximize','使最大化','作者选择追求自身最大的幸福','We try to maximize the benefit of each lesson.','maximize happiness','maximize the benefit'),
'q-c01-021':vocab('eudaimonic approach','实现论取向','侧重有意义生活的研究取向','The eudaimonic approach considers purpose and development.','the eudaimonic approach','eudaimonic well-being'),
'q-c01-028':vocab('existential crisis','存在危机；对人生意义的深刻疑问','外在生活顺利时仍出现的意义危机','The novel follows a writer facing an existential crisis.','experience an existential crisis','a sudden existential crisis'),
'q-c01-029':vocab('adds up','累积；不断增加','职业全垒打总数类比经历的积累','A few minutes of practice every day adds up.','it all adds up','add up over time'),
'q-c02-021':vocab('in-state tuition','州内学费','例子中选择 UVA 的一个实际考虑','Students may qualify for in-state tuition.','pay in-state tuition','qualify for in-state tuition'),
'q-c02-022':vocab('smashing success','极大的成功','取得成功后财富目标仍不断提高','The concert was a smashing success.','a smashing success','become a smashing success')}
active=[];protected={}
for base in old:
 q=copy.deepcopy(base);lo,hi,zh=R[q['id']];group=ss[lo:hi+1];p=paragraphs[q['paragraphId']]
 assert group and all(s['paragraphId']==p['id'] for s in group),(q['id'],'paragraph mismatch')
 passage=p['text'][group[0]['start']:group[-1]['end']];assert words(passage)<=110,(q['id'],words(passage))
 q.update(version=2,passage=passage,sentenceIds=[s['id'] for s in group],translation=zh)
 for field in ('explanation','grammar','strategy'):q.pop(field,None)
 q['evidence']=[e for e in q['evidence'] if e['quote'] in passage]
 assert q['evidence'],('Review evidence',q['id'])
 q['vocabulary']=[v for v in q['vocabulary'] if v['word'].lower() in passage.lower()]
 if not q['vocabulary']:q['vocabulary']=[extra[q['id']]]
 q['editorialStatus']='短段版 v2；连续原句，配题片段互不重叠；保留 v1 历史快照，不重算旧成绩'
 if q['id']=='q-c01-001':q['analyses']=['A 原句没有“大米出口和垒球队使当地闻名”的信息。','B 直接对应 known for its green tea and clementines。','C 原句没有说农业高中使该地闻名。','D 原句没有说年度赏樱聚会使当地闻名。']
 if q['id']=='q-c02-021':q['analyses']=['A everything I want 表明该选择满足自身需要，且只申请 UVA。','B could probably get into...elite schools 说明并非成绩不足。','C 原文的选择理由是满足需求及州内学费，不是声望至上。','D 原文只申请 UVA，并未先申请每所学校再比最低价格。']
 if q['id']=='q-c02-010':q['analyses']=['A 心理免疫系统是类比，不能改成生物病毒直接造成所有不幸福。','B 本句没有禁止讨论负面心情，never 的说法缺乏证据。','C Although...are effective 明确承认主动策略有效，和 always ineffective 相反。','D natural ability to heal and recover 明确支持从负面情绪中自然恢复的能力。']
 for s in group:assert s['id'] not in protected,('Duplicate question sentence',q['id'],s['id']);protected[s['id']]=q['id']
 active.append(q)
units=[]
def append(group,qid=None):
 if not group:return
 p=paragraphs[group[0]['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 units.append(dict(id=p['id']+'-r'+group[0]['id'].rsplit('-s',1)[1]+'-'+group[-1]['id'].rsplit('-s',1)[1],chapterId=p['chapterId'],sectionId=p['sectionId'],paragraphId=p['id'],sentenceIds=[s['id'] for s in group],wordCount=words(text),questionId=qid,pdfPages=sorted({r['pdfPage'] for s in group for r in s['sources']})))
for p in b['paragraphs']:
 group=[byid[i] for i in p['sentenceIds']];i=0
 while i<len(group):
  owner=protected.get(group[i]['id']);chunk=[group[i]];i+=1
  if owner:
   while i<len(group) and protected.get(group[i]['id'])==owner:chunk.append(group[i]);i+=1
  else:
   while i<len(group) and not protected.get(group[i]['id']) and len(chunk)<4 and sum(words(s['text']) for s in chunk)+words(group[i]['text'])<=90:chunk.append(group[i]);i+=1
  append(chunk,owner)
flattened=[sid for u in units for sid in u['sentenceIds']]
assert flattened==[s['id'] for s in ss],'Missing, repeated or reordered sentences'
assert max(u['wordCount'] for u in units)<=110,'Do not split an original sentence silently'
unit_by_q={u['questionId']:u for u in units if u['questionId']}
additional_path=ROOT/'source/short-questions/additional.json'
if additional_path.exists():
 for q in load('source/short-questions/additional.json'):
  assert q['id'] not in {x['id'] for x in active},('Duplicate question ID',q['id'])
  u=next(u for u in units if u['id']==q['readingUnitId']);assert not u['questionId'],('Unit already has a question',u['id'])
  p=paragraphs[u['paragraphId']];group=[byid[i] for i in u['sentenceIds']]
  assert q['sentenceIds']==u['sentenceIds'] and q['passage']==p['text'][group[0]['start']:group[-1]['end']]
  u['questionId']=q['id'];active.append(q);unit_by_q[q['id']]=u
active.sort(key=lambda q:min(position[i] for e in q['evidence'] for i in e['sentenceIds']))
def canonical_numbers(v):
 if isinstance(v,float) and v.is_integer():return int(v)
 if isinstance(v,list):return [canonical_numbers(x) for x in v]
 if isinstance(v,dict):return {k:canonical_numbers(x) for k,x in v.items()}
 return v
active=canonical_numbers(active)
catalog=load('src/data/passage-translations.json');entries=catalog['entries'];known={(e['questionId'],e['sourceFingerprint']) for e in entries}
for q in active:
 unit=unit_by_q[q['id']];q['readingUnitId']=unit['id'];q.pop('fingerprint',None)
 q['fingerprint']=hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if (q['id'],q['fingerprint']) not in known:entries.append(dict(questionId=q['id'],passage=q['passage'],sourceFingerprint=q['fingerprint'],translation=q['translation']))
plan=dict(version=1,pdfSha256=b['pdfSha256'],rule='同一来源段落内连续原句；一般不超过 90 词；不切断原句或完整证据，少量片段最多 110 词。每个候选句按原书顺序恰好出现一次。',coverage=dict(totalCandidateSentences=len(ss),includedSentences=len(flattened),duplicateSentenceIds=[],missingSentenceIds=[],units=len(units),unitsWithQuestions=len(active),unitsWithoutQuestions=len(units)-len(active),maxWords=max(u['wordCount'] for u in units),over90Words=[u['id'] for u in units if u['wordCount']>90],allSentencesIncluded=True,allQuestionsPrepared=False),units=units)
catalog['entries']=list({(e['questionId'],e['passage']):e for e in entries}.values())
save('public/data/questions.json',active);save('public/data/reading-plan.json',plan);save('src/data/passage-translations.json',catalog)
runpy.run_path(str(ROOT/'scripts/batches/question-translations.py'),run_name='__main__')
print(json.dumps(plan['coverage'],ensure_ascii=False))
