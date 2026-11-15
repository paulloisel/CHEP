"""Assemble the bounded P02 evidence batches; never writes outside P02."""
import csv,json,re,unicodedata
from collections import Counter,defaultdict
from pathlib import Path

R=Path(__file__).resolve().parent
OUT=R.parent
def read(name): return json.loads((R/name).read_text())
def norm(x): return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',str(x)).encode('ascii','ignore').decode().lower())
def parts(x):
    if isinstance(x,list): return x
    return [s.strip() for s in str(x or '').split(';') if s.strip()]
def unique(items): return list(dict.fromkeys(items))
def write(name,rows,fields):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)

feat=read('featured.json'); fellows=read('fellows.json'); roster=read('roster.json'); levy=read('levy.json'); cord=read('cordelli.json')
source_rows=[]
for d in [roster,feat,fellows,levy,cord]: source_rows.extend(d['sources'])
source_rows.extend(read('site_sources.json'))
if (R/'qa_sources.json').exists(): source_rows.extend(read('qa_sources.json'))
sources={x['source_id']:x for x in source_rows}

cohort=[]
for n,c in enumerate(roster['cohort'],1):
    c=dict(c);c['person_id']=f'P02-P{n:03}';c['as_of_date']='2026-11-15'
    if c['name']=='Paul-André Rosental':
        c['inclusion_category']='core: scientific council member'
        c['Paris_connection']='Sciences Po institutional profile lists membership of Centre for History and Economics-Paris scientific council'
        c['connection_dates']='date_unknown; role listed in accessed institutional profile'
        c['evidence_status']='verified';c['source_ids']+=';P02-SF031'
    cohort.append(c)
name_to_person={norm(c['name']):c for c in cohort}
def people_for(row):
    names=parts(row.get('person_ids',row['authors']))
    found=[]
    for name in names:
        cleaned=re.sub(r'\s*\([^)]*\)','',name)
        c=name_to_person.get(norm(cleaned))
        if c: found.append(c)
    if not found:
        for c in cohort:
            if norm(c['name']) in norm(row['authors']): found.append(c)
    return unique([c['person_id'] for c in found])
pid_to_person={c['person_id']:c for c in cohort}

raw=[]
for prefix,rows in [('F',feat['records']),('RF',fellows['publications']),('C',cord['records']),('L',levy['records'])]:
    for r in rows:
        q=dict(r);q['_batch']=prefix;raw.append(q)
# Apply one consistent interview policy across authors: verified published text
# interviews are included with contributor roles, while uncertain appearances stay separate.
for s in cord.get('supplementary',[]):
    if s.get('type')=='published_interview' and s.get('verification_status')=='verified':
        raw.append(dict(record_id=s['record_id'],work_id='P02-CWINTERVIEW',edition_or_version_id='P02-CEINTERVIEW',title=s['title'],authors=s['authors'],person_ids='Chiara Cordelli',type='interview',first_publication_year=s['date'][:4],edition_date=s['date'],venue_or_publisher='Forward / Recenti Progressi in Medicina',language='Italian',DOI_or_ISBN='not_found_publicly',canonical_url=s['canonical_url'],open_access_url=s['canonical_url'],themes='privatization;democracy',period_studied='not_applicable',geography_studied='not_applicable',CHEP_relationship='published_during_documented_affiliation',affiliation_evidence='CHEP visitor 2025–2027',support_evidence='not_found_publicly',verification_status='verified',source_ids=s['source_ids'],metadata_notes='Published text interview; interviewer and interviewee roles retained. Included consistently with the other authors’ interviews.',_batch='C'))
supp=[]
for d in [fellows,cord,levy]:
    for s in d.get('supplementary',[]):
        if s.get('type')!='published_interview': supp.append(dict(s))
for s in cord.get('theses',[]): supp.append(dict(s,type='thesis'))

def titlekey(r):
    s=norm(r['title'])
    if s.startswith('souslesverrous'): return 'souslesverrous'
    return s
dedup={}; rows=[]; crosses=[]; rawwork_to_final={}
for r in raw:
    oldid=r['record_id']
    if oldid in ['P02-RF060','P02-L020']:
        supp.append(dict(title=r['title'],authors=r['authors'],year=r['first_publication_year'],type='unresolved_contribution' if oldid=='P02-RF060' else 'unresolved_public_text_series',reason=r.get('evidence_note','Distinct individual text not identified; volume contribution attested'),source_ids=r['source_ids'],status='unverified',original_record_id=oldid));continue
    key=titlekey(r)
    existing=dedup.get(key)
    refs=parts(r['source_ids'])
    note=r.get('evidence_note',r.get('metadata_notes',''))
    if existing:
        existing['source_ids']=';'.join(unique(parts(existing['source_ids'])+refs))
        existing['person_ids']=';'.join(unique(parts(existing['person_ids'])+people_for(r)))
        existing['evidence_note']=' | '.join(unique([existing['evidence_note'],note]))
        if r['_batch']=='RF' and existing['DOI_or_ISBN']=='not_found_publicly': existing['DOI_or_ISBN']=str(r['DOI_or_ISBN'])
        crosses.append(dict(input_record_id=oldid,record_id=existing['record_id'],work_id=existing['work_id'],decision='merged_same_text_or_edition'))
        rawwork_to_final[(r['_batch'],r['work_id'])]=existing['work_id']
        continue
    q=dict(r);q['record_id']=f'P02-R{len(rows)+1:03}';q['edition_or_version_id']=f'P02-E{len(rows)+1:03}'
    rawwork=(r['_batch'],r['work_id'])
    if rawwork not in rawwork_to_final: rawwork_to_final[rawwork]=f'P02-W{len(set(rawwork_to_final.values()))+1:03}'
    q['work_id']=rawwork_to_final[rawwork];q['person_ids']=';'.join(people_for(q))
    q['type']={'chapter':'book_chapter','review_essay':'review','encyclopedia_entry':'reference_entry','article':'journal_article','public_essay':'public_scholarship','edited_book':'edited_volume'}.get(q['type'],q['type'])
    q['first_publication_year']=str(q['first_publication_year']);q['edition_date']=str(q['edition_date'])
    q['language']={'en':'English','fr':'French','it':'Italian','de':'German','es':'Spanish'}.get(q.get('language'),q.get('language','not_found_publicly'))
    q['featured_on_publications_page']='yes' if r['_batch']=='F' else 'no'
    q['evidence_note']=note or 'Bibliographic metadata only.'
    if oldid in ['P02-C024','P02-C025','P02-C026','P02-C027','P02-C028']:
        q['evidence_note']=q['evidence_note'].replace(' Philanthropy chapter: author lists 2017; online publication 2016-12-22.','')
    q['content_basis']=q.get('content_basis','publisher_description_or_author_synopsis' if r['_batch']=='F' else 'metadata_only')
    q['content_basis']={'P02-C001':'author_book_synopsis','P02-C004':'publisher_description','P02-C005':'abstract_and_introduction','P02-C006':'abstract','P02-C008':'abstract','P02-C035':'full_public_text','P02-RF067':'abstract_and_introduction','P02-RF068':'abstract','P02-RF064':'full_public_text','P02-RF063':'interview_text','P02-RF017':'indexed_publisher_abstract'}.get(oldid,q['content_basis'])
    q['as_of_date']='2026-11-15';q['count_in_published_text_total']='yes'
    for field in ['canonical_url','open_access_url','support_evidence','themes','period_studied','geography_studied','affiliation_evidence','DOI_or_ISBN']:
        if not q.get(field): q[field]='not_found_publicly'
    if 'format=cv' in q['canonical_url'] or 'cv.hal.science' in q['canonical_url'] or 'medias/fichier/le-bras-liste-publications' in q['canonical_url'] or 'CurriculumVitae' in q['canonical_url'] or q['canonical_url'].endswith('/cordelli'):
        q['evidence_note']+=' Work-specific canonical URL not recovered; supporting bibliography retained in source register.'
        q['canonical_url']='not_found_publicly'
    # Conservative institutional attribution; featured status has priority, funding never inferred.
    personrows=[pid_to_person[p] for p in parts(q['person_ids'])]
    core=[p for p in personrows if p['inclusion_category'].startswith('core:')]
    q['cohort_for_counting']='core_affiliate' if core else 'wider_featured_only'
    if q['featured_on_publications_page']=='yes':
        q['CHEP_relationship']='featured_participant_publication'
    elif any(p['name']=='Chiara Cordelli' for p in personrows):
        q['CHEP_relationship']='published_during_documented_affiliation' if q['edition_date'][:4]=='2026' else ('relationship_unresolved' if q['edition_date'][:4]=='2025' else 'affiliate_earlier_scholarship')
        if q['edition_date'][:4]=='2025': q['evidence_note']+=' Publication in starting year 2025; exact appointment start unknown, so during-affiliation status is unresolved.'
    elif any(p['name']=='Dev Patel' for p in personrows) and q['edition_date'][:4]=='2022':
        q['CHEP_relationship']='relationship_unresolved'
        q['evidence_note']+=' May 2022 essay overlaps visiting-student years 2021–2022; exact end date unverified.'
    elif any(p['name']=='Liane Hewitt' for p in personrows) and q['edition_date'][:4] in ['2024','2025']:
        q['CHEP_relationship']='relationship_unresolved'
        q['evidence_note']+=' Publication year overlaps 2024–2025 fellowship, but exact start/end dates are not established; period attribution remains unresolved.'
    elif any(p['name']=='Liane Hewitt' for p in personrows) and q['edition_date'][:4].isdigit() and int(q['edition_date'][:4])<2024:
        q['CHEP_relationship']='affiliate_earlier_scholarship'
    elif any(p['name']=='Elsa Génard' for p in personrows) and q['edition_date'][:4] in ['2021','2022']:
        q['CHEP_relationship']='relationship_unresolved'
        q['evidence_note']+=' Publication year overlaps 2021–2022 fellowship, but exact dates are not established; period attribution remains unresolved.'
    elif any(p['name']=='Elsa Génard' for p in personrows) and q['edition_date'][:4].isdigit() and int(q['edition_date'][:4])<2021:
        q['CHEP_relationship']='affiliate_earlier_scholarship'
    elif q['first_publication_year'].isdigit() and int(q['first_publication_year'])<2019:
        q['CHEP_relationship']='affiliate_earlier_scholarship'
    elif q['title']=='Times of Drought': q['CHEP_relationship']='featured_participant_publication'
    else: q['CHEP_relationship']='relationship_unresolved'
    q['affiliation_evidence']=' | '.join(f"{p['person_id']}: {p['inclusion_category']}; {p['connection_dates']}; sources {p['source_ids']}" for p in personrows) or 'not_found_publicly'
    q['source_ids']=';'.join(unique(refs+[sid for p in personrows for sid in parts(p['source_ids'])]))
    if any(p['name']=='Anatole Le Bras' for p in personrows) and q['CHEP_relationship']!='featured_participant_publication':
        q['CHEP_relationship']='relationship_unresolved';q['evidence_note']+=' Le Bras fellowship dates conflict; no precise during-affiliation attribution made.'
    q['evidence_url']=sources[refs[0]]['url'] if refs and refs[0] in sources else 'not_found_publicly'
    q['source_title']=sources[refs[0]]['title'] if refs and refs[0] in sources else 'not_found_publicly'
    rows.append(q);dedup[key]=q
    crosses.append(dict(input_record_id=oldid,record_id=q['record_id'],work_id=q['work_id'],decision='retained_edition_or_version'))

# Apply independent QA against responsible sources without altering intermediates.
for q in rows:
    if '/autore/chiara-cordelli-' in q['canonical_url']:
        item_sources=[sources[s] for s in parts(q['source_ids']) if s in sources and '/editorialedomani.it/' not in sources[s]['url'] and 'editorialedomani.it/' in sources[s]['url'] and '/autore/' not in sources[s]['url']]
        if item_sources:q['canonical_url']=item_sources[0]['url']
    if q['type']=='book_chapter' and q['canonical_url']=='https://press.uchicago.edu/ucp/books/book/chicago/P/bo23530413.html':
        q['canonical_url']='not_found_publicly';q['evidence_note']+=' Publisher contents page is a container URL, not a chapter identifier; retained in sources.'
    if q['record_id']=='P02-R001':
        q['evidence_note']=q['evidence_note'].replace('exact day and identifier not independently verified.','exact day not independently verified in the original publisher check; DOI 10.4000/14x0b is attested in the inspected HAL bibliography.')
    if q['title'].startswith('From Fiscal Triangle') and 'P02-SQ002' in sources:
        q['venue_or_publisher']='Corporations and American Democracy (Naomi R. Lamoreaux and William J. Novak, eds.); Harvard University Press, 213–244'
        q['canonical_url']=sources['P02-SQ002']['url'];q['source_ids']+=';P02-SQ002';q['verification_status']='verified'
        q['evidence_note']='Responsible project publisher/contents page confirms Harvard University Press; corrects Cambridge University Press in old CV. Chapter metadata, not full text, read.'
    if q['title'].startswith('The World in Blocs') and 'P02-SQ001' in sources:
        q['edition_date']='2022-12-19';q['venue_or_publisher']='Journal of Global History 18(2), July 2023, 236–258'
        q['canonical_url']=sources['P02-SQ001']['url'];q['open_access_url']=q['canonical_url'];q['source_ids']+=';P02-SQ001';q['verification_status']='verified'
        q['evidence_note']='First online 2022-12-19, issue July 2023; one article. Publisher marks CC BY.'
    if q['title'].startswith('Psychiatrists, addicted patients') and 'P02-SQ007' in sources:
        q['title']='Psychiatrists, Addicted Patients, and Institutions of Care: European Histories from the Nineteenth and Twentieth Centuries'
        q['DOI_or_ISBN']='10.1086/737536';q['canonical_url']=sources['P02-SQ007']['url'];q['source_ids']+=';P02-SQ007'
        q['edition_date']='2025-11-12';q['venue_or_publisher']='The Social History of Alcohol and Drugs 39(2), 141–151'
        q['evidence_note']='Guest editors’ introduction; issue September 2025; publisher online date 2025-11-12. Bibliographic metadata verified; no separate special-issue work added. Le Bras affiliation dates remain conflicting.'
    if q['title'].startswith('Routines punitives') and 'P02-SQ005' in sources:
        q['edition_date']='2023-10-05';q['DOI_or_ISBN']+='; ISBN 9782271133113';q['source_ids']+=';P02-SQ005';q['canonical_url']=sources['P02-SQ005']['url']

coverage=[]
cov_by_name={norm(c['name']):c for c in fellows['author_coverage']}
for c in cohort:
    mine=[r for r in rows if c['person_id'] in parts(r['person_ids'])]
    refs=unique([sid for r in mine for sid in parts(r['source_ids'])]+parts(c['source_ids']))
    entry=dict(person_id=c['person_id'],cohort='core' if c['inclusion_category'].startswith('core:') else 'wider_featured',sources_checked=';'.join(refs),years_covered='not_yet_bibliographically_checked',output_types_checked='not_yet_bibliographically_checked',gaps='Career bibliography; institutional CV/repository; ORCID identity; publisher identifiers and dated affiliation remain queued.',completion_status='roster_checked_bibliography_queued')
    if mine:
        years=sorted(set(r['first_publication_year'] for r in mine))
        entry.update(years_covered=';'.join(years),output_types_checked=';'.join(sorted(set(r['type'] for r in mine))),completion_status='featured_or_targeted_items_checked_career_not_expanded')
    if norm(c['name']) in cov_by_name:
        entry.update({k:v for k,v in cov_by_name[norm(c['name'])].items() if k!='name'})
        entry['sources_checked']=';'.join(unique(parts(entry['sources_checked'])+refs))
    if c['name']=='Jonathan Levy':
        entry.update(completion_status='named_CV_text_entries_extracted_plus_targeted_updates; not_career_complete',gaps='CV currentness unknown (apparent 2022 cutoff); current 2023–2026 article/chapter census unclosed; untitled Nobody’s Property contribution and inaccessible Houston series excluded; complete outlet archives and translations unclosed; no historian ORCID verified.',years_covered='2006–2026; CV 2006–2022 plus publisher and outlet updates',output_types_checked='monographs;articles;chapters;reviews;essays;interviews')
    if c['name']=='Chiara Cordelli':
        cc=cord.get('coverage',{})
        entry.update(completion_status='current_author_lists_and_accessible_outlet_batch_extracted; residual_queue',gaps='Full current DOCX CV inaccessible; second Domani archive page and individual coauthor/version details remain queued; see research/cordelli_notes.md.',years_covered='2010–2026; year/date_unknown retained where necessary',output_types_checked='monographs;edited volumes;articles;chapters;public essays;book excerpt')
    if c['inclusion_category'].startswith('wider:'):
        entry['gaps']='Career expansion excluded by design; retain only CHEP-featured or separately documented Paris-connected work. Current Paris committee role unresolved except Rosental separately verified.'
        entry['completion_status']='complete_featured_page_batch; not_career_census'
    entry['catalogue_records']=len(mine);entry['as_of_date']='2026-11-15';coverage.append(entry)

for n,s in enumerate(supp,1):
    s['supplementary_id']=f'P02-X{n:03}';s['as_of_date']='2026-11-15';s['count_in_published_text_total']='no'
    s['year']=s.get('year',s.get('first_publication_year',s.get('date','date_unknown')))
    s['reason']=s.get('reason',s.get('notes',s.get('metadata_notes',s.get('status','Outside published-text scope'))))
    s['verification_status']=s.get('verification_status','unverified' if 'unresolved' in s.get('type','') else 'verified')
    s['source_ids']=';'.join(parts(s.get('source_ids','')))

pubfields='record_id,work_id,edition_or_version_id,title,authors,person_ids,type,first_publication_year,edition_date,venue_or_publisher,language,DOI_or_ISBN,canonical_url,open_access_url,themes,period_studied,geography_studied,CHEP_relationship,affiliation_evidence,support_evidence,verification_status,source_ids,featured_on_publications_page,cohort_for_counting,content_basis,evidence_note,evidence_url,source_title,as_of_date,count_in_published_text_total'.split(',')
write('publications.csv',rows,pubfields)
write('cohort.csv',cohort,'person_id,name,inclusion_category,Paris_connection,connection_dates,evidence_status,source_ids,as_of_date'.split(','))
write('author_coverage.csv',coverage,'person_id,cohort,sources_checked,years_covered,output_types_checked,gaps,completion_status,catalogue_records,as_of_date'.split(','))
write('sources.csv',sources.values(),'source_id,url,title,publisher_or_owner,source_date,accessed_at,source_type,supports,retrieval_status'.split(','))
write('supplementary.csv',supp,'supplementary_id,title,authors,type,year,reason,verification_status,source_ids,as_of_date,count_in_published_text_total'.split(','))
write('record_crosswalk.csv',crosses,'input_record_id,record_id,work_id,decision'.split(','))

workrows={}
rank={'monograph':0,'short_monograph':1,'edited_volume':2,'methods_book':3}
for r in rows:
    old=workrows.get(r['work_id'])
    if old is None or rank.get(r['type'],9)<rank.get(old['type'],9):workrows[r['work_id']]=r
def period(y):
    if not str(y).isdigit():return 'date_unknown'
    y=int(y)
    return 'before_2019' if y<2019 else ('2019–2021' if y<=2021 else ('2022–2025' if y<=2025 else '2026_to_cutoff'))
stats=dict(records=len(rows),works=len(workrows),featured_records=sum(r['featured_on_publications_page']=='yes' for r in rows),featured_works=len(set(r['work_id'] for r in rows if r['featured_on_publications_page']=='yes')),cohort_people=len(cohort),core_people=sum(c['inclusion_category'].startswith('core:') for c in cohort),wider_people=sum(c['inclusion_category'].startswith('wider:') for c in cohort),represented_people=len(set(p for r in rows for p in parts(r['person_ids']))),source_records=len(sources),unique_source_urls=len(set(s['url'] for s in sources.values())),supplementary=len(supp),records_by_type=dict(Counter(r['type'] for r in rows)),works_by_type=dict(Counter(r['type'] for r in workrows.values())),records_by_cohort=dict(Counter(r['cohort_for_counting'] for r in rows)),works_by_cohort=dict(Counter(r['cohort_for_counting'] for r in workrows.values())),works_by_first_year_period=dict(Counter(period(r['first_publication_year']) for r in workrows.values())),records_by_edition_period=dict(Counter(period(r['edition_date'][:4]) for r in rows)),records_by_relationship=dict(Counter(r['CHEP_relationship'] for r in rows)),verification_status=dict(Counter(r['verification_status'] for r in rows)))
R.joinpath('stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2))
print(json.dumps(stats,ensure_ascii=False,indent=2))
# Referential-integrity checks matter: source and person IDs must resolve.
missing_s=sorted({s for r in rows+cohort+supp for s in parts(r.get('source_ids','')) if s not in sources})
missing_p=sorted({p for r in rows for p in parts(r['person_ids']) if p not in pid_to_person})
assert not missing_s,missing_s
assert not missing_p,missing_p
assert len(set(r['record_id'] for r in rows))==len(rows)
assert stats['featured_records']==18 and stats['featured_works']==14
assert all(r['person_ids'] for r in rows)
assert all(r['verification_status'] in {'verified','inferred','conflicting','unverified'} for r in rows)
print('PASS: source/person references, unique record IDs, 18 featured editions / 14 works, evidence statuses.')
