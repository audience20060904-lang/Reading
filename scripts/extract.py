"""Deterministic candidate extraction. Never labels automated output as proofread.
Usage: python scripts/extract.py PATH_TO_PDF. Requires pymupdf==2.0.
Keep source/pages.json and source/layout.json for provenance. See CONTENT.md.
"""
from pathlib import Path
import sys, json, re, hashlib, unicodedata
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
def norm(s):
 # Only whitespace / ligature encoding changes. Preserve visible hyphens.
 return re.sub(r'\s+',' ',unicodedata.normalize('NFC',s).translate(str.maketrans({'ﬁ':'fi','ﬂ':'fl','ﬀ':'ff','ﬃ':'ffi','ﬄ':'ffl'}))).strip()
def split_sentences(t):
 # Candidate boundary detector, deliberately not a proofreading claim.
 spans=[]; start=0
 for m in re.finditer(r'[.!?][”’\"\)]*(?:\s+|$)',t):
  end=m.end(); before=t[:m.start()+1]
  if re.search(r'(?:\b(?:Mr|Mrs|Ms|Dr|Prof|St|vs|e\.g|i\.e|etc)|\b[A-Z]|\bU\.S)\.$',before): continue
  if t[m.start():m.start()+3]=='...': continue
  e=m.start()+len(m.group().rstrip()); a=start
  while a<e and t[a].isspace(): a+=1
  if e>a: spans.append((a,e))
  start=end
 if t[start:].strip(): spans.append((start+len(t[start:])-len(t[start:].lstrip()),len(t)))
 return spans
pdf=Path(sys.argv[1]); doc=pymupdf.open(pdf)
pages=[]; layouts=[]; chapters=[]; sections=[]; paras=[]; excluded=[]; chapter=None; section=None; last=None; active=False
for pi,page in enumerate(doc):
 pn=pi+1; raw=page.get_text(); pages.append({'pdfPage':pn,'raw':raw})
 blocks=[b for b in page.get_text('dict')['blocks'] if 'lines' in b]; layouts.append({'pdfPage':pn,'blocks':blocks})
 if pn<7: excluded.append({'pdfPage':pn,'kind':'front-matter','reason':'封面、版权、目录、题献；保留原始提取，不计正文句子'}); continue
 if raw.startswith('ACKNOWLEDGMENTS') or raw.startswith('Acknowledgments'): active=False
 if raw.startswith('CHAPTER '):
  ci=len(chapters)+1; chapter={'id':f'c{ci:02}','number':ci,'title':'','pdfPage':pn,'sectionIds':[]};chapters.append(chapter);section=None;last=None;active=True
 if not active: excluded.append({'pdfPage':pn,'kind':'back-matter','reason':'致谢、注释、附录、索引、作者介绍或出版推广，不计正文候选句子'});continue
 for bi,b in enumerate(blocks):
  lines=b['lines']; texts=[''.join(s['text'] for s in l['spans']) for l in lines]; text=norm(' '.join(texts)); size=max(s['size'] for l in lines for s in l['spans']); first=lines[0]['spans'][0]
  if text.startswith('CHAPTER '): excluded.append({'pdfPage':pn,'block':bi,'kind':'chapter-label','reason':'章节标记'});continue
  if not section and size>16:
   chapter['title']+=' '+text; chapter['title']=chapter['title'].strip();excluded.append({'pdfPage':pn,'block':bi,'kind':'chapter-title','reason':'标题单独存储'});continue
  if re.match(r'^\d+\. ',text) and size<14:
   si=len(chapter['sectionIds'])+1; section={'id':f"{chapter['id']}-s{si:02}",'number':si,'title':text,'chapterId':chapter['id'],'pdfPage':pn,'paragraphIds':[]};sections.append(section);chapter['sectionIds'].append(section['id']);last=None;continue
  if not section:
   excluded.append({'pdfPage':pn,'block':bi,'kind':'epigraph-or-subtitle','text':text,'reason':'章首引文、出处、章副标题；保留文本，不作为实验结论或正文计数'}); continue
  if size<14:
   excluded.append({'pdfPage':pn,'block':bi,'chapterId':chapter['id'],'sectionId':section['id'],'kind':'table-or-subheading','text':text,'reason':'正文表格、图注或非编号小标题，保留原文待结构化；暂不计叙事候选句子，不代表非正文或已完成内容'});last=None;continue
  # page-leading flush-left text is a continuation; an indented line starts a paragraph.
  continuation=last is not None and last['sources'][-1]['pdfPage']!=pn and first['bbox'][0]<85
  text=norm(re.sub(r'-\n(?=\w)','-', '\n'.join(texts)))
  chunk={'pdfPage':pn,'block':bi,'bbox':[round(v,2) for v in b['bbox']],'raw':'\n'.join(texts),'text':text}
  if continuation:
   last['text']+=' '+text;last['sources'].append(chunk);last['raw']+='\n\f\n'+'\n'.join(texts)
  else:
   ident=f"{section['id']}-p{pn:03}-{round(b['bbox'][1]*10):05}"
   last={'id':ident,'chapterId':chapter['id'],'sectionId':section['id'],'text':text,'raw':'\n'.join(texts),'sources':[chunk],'sentenceIds':[]};paras.append(last);section['paragraphIds'].append(ident)
sentences=[]
for p in paras:
 for i,(a,b) in enumerate(split_sentences(p['text'])):
  sid=f"{p['id']}-s{i+1:03}"; p['sentenceIds'].append(sid)
  # Source pages determined by normalized character offsets, including cross-page sentences.
  off=0; refs=[]
  for chunk in p['sources']:
   end=off+len(chunk['text'])
   if a<end and b>off: refs.append({'pdfPage':chunk['pdfPage'],'block':chunk['block'],'bbox':chunk['bbox']})
   off=end+1
  sentences.append({'id':sid,'chapterId':p['chapterId'],'sectionId':p['sectionId'],'paragraphId':p['id'],'text':p['text'][a:b],'start':a,'end':b,'sources':refs,'review':'candidate'})
book={'id':'life-three-dimensions','title':'Life in Three Dimensions: How Curiosity, Exploration, and Experience Make a Fuller, Better Life','author':'Shigehiro Oishi','pdfSha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdfPages':len(doc),'extractionVersion':'layout-v1','normalization':'合并排版断行为空格；NFC；展开 fi/fl/ff/ffi/ffl 合字；保留可见连字符、大小写和标点；跨页段落按首行缩进识别，所有分句均为候选。raw 与坐标完整保留。','chapters':chapters,'sections':sections,'paragraphs':paras,'sentences':sentences,'excluded':excluded}
save(ROOT/'source/pages.json',pages);save(ROOT/'source/layout.json',layouts);save(ROOT/'public/data/book.json',book)
print(json.dumps({'pages':len(doc),'chapters':len(chapters),'sections':len(sections),'paragraphs':len(paras),'candidateSentences':len(sentences)},ensure_ascii=False))
