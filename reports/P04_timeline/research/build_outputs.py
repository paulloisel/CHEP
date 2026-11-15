import csv, json, re
from pathlib import Path
from collections import Counter, defaultdict

BASE = Path(__file__).resolve().parent.parent
R = BASE / 'research'
def readcsv(p):
    with p.open(encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
def readjson(p): return json.loads(p.read_text())
def writecsv(name, rows, fields):
    with (BASE/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader(); w.writerows(rows)

sources=readjson(R/'seminars/sources.json')
for p in ['origins/sources.csv','partners/partner_sources.csv','partners/extra_sources.csv','workshops/sources.csv']:
    sources += readcsv(R/p)
source_by_id={r['source_id']:r for r in sources}
assert len(source_by_id)==len(sources)
events=readjson(R/'seminars/events.json')+readjson(R/'seminars/extra_event.json')
for p,series,group in [('partners/joint_seminars.csv','Joint Centre online seminar','joint_online_network'),('partners/extra_events.csv','Climate and Capitalism','paris_centre_programme'),('workshops/events.csv','CHEP workshops and other events','paris_centre_programme'),('origins/atelier_unverified_leads.csv','L’atelier du CHEP','unverified_lead')]:
    for row in readcsv(R/p):
        row['series']=series; row['census_group']=group
        events.append(row)
for e in events:
    old=e['event_id']; e['source_record_id']=old
    if 'census_group' not in e:
        e['census_group']='paris_supported_series' if old.startswith('P04-SH') else 'linked_host_series' if old.startswith('P04-SM') else 'paris_centre_programme'
    e['counted_in_census']='false' if e['census_group']=='unverified_lead' else 'true'
    dates=e['dates']
    if 'date_start' not in e:
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}/\d{4}-\d{2}-\d{2}',dates):
            e['date_start'],e['date_end']=dates.split('/'); e['date_precision']='day_range'
        elif re.fullmatch(r'\d{4}-\d{2}-\d{2}',dates):
            e['date_start']=e['date_end']=dates; e.setdefault('date_precision','day')
        elif dates.startswith('2020 '):
            e['date_start']=e['date_end']='2020'; e['date_precision']='year'
        elif dates.startswith('2025 '):
            e['date_start']=e['date_end']='2025-spring';e['date_precision']='season'
        else: raise ValueError(dates)
    e['temporal_scope']='rescheduled_date_unknown' if e['date_start']=='date_unknown' else 'future' if e['date_start'][:10]>'2026-11-15' else 'historical'
    e.setdefault('evidence_notes',e.get('evidence_note','not_found_publicly'))
    e.setdefault('as_of_date','2026-11-15')
    if old in ['W002','W003','W004','W005','W011']:
        people=e['speakers']; e['evidence_notes']+=' Authors/paper authors mentioned as subjects: '+people+'.'
        e['speakers']={'W002':'Jeremy Adelman; Odette Lienau (commentators)','W003':'Claire Lemercier; Paul-André Rosental (commentators)','W004':'Mary O’Sullivan (commentator)','W005':'not_found_publicly','W011':'Arnaud Houte (presentation)'}[old]
    if old=='W018': e['evidence_notes']+=' Venue is inferred separately from verified day/occurrence.'
    ids=e['source_ids'].split(';')
    assert all(i in source_by_id for i in ids),(old,ids)
    e['source_urls']=';'.join(dict.fromkeys(source_by_id[i]['url'] for i in ids))
events.sort(key=lambda e:(e['date_start']=='date_unknown',e['date_start'],e['title']))
for i,e in enumerate(events,1): e['event_id']=f'P04-E{i:03d}'
fields=['event_id','title','dates','status','format','speakers','organisers','partners','CHEP_role','topics','language','location_or_mode','programme_url','recording_url','source_ids','evidence_status','evidence_notes','date_start','date_end','date_precision','temporal_scope','series','census_group','counted_in_census','source_record_id','source_urls','as_of_date']
for e in events:
    for k in fields: e.setdefault(k,'not_found_publicly')
writecsv('events.csv',events,fields)

milestones=readcsv(R/'origins/milestones.csv')
for row in milestones:
    row['source_record_id']=row['milestone_id']; row['as_of_date']='2026-11-15'
    if row['milestone_id']=='P04-HM009':
        row.update(date_start='2022-09-12',date_end='2022-09-12',date_precision='day_announcement',source_ids=row['source_ids']+';P04-S004')
add=[
('2020-05-20','joint_online_programme','Earliest session in checked Joint Centre online archive: Emma Rothschild on cholera and historical distance.','Cambridge; Harvard; Paris','Dates the checked network series; announcement only.','P04-N001;P04-N002'),
('2022-07-11','environmental_programme','CHEP hosted an economic/environmental history roundtable.','CHEP','Early documented held climate-related exchange.','P04-W001;P04-W002'),
('2022-11-09','junior_research','CHEP-supported Valuing Empires conference opened.','CHEP; CHSP','Junior conference support; held evidence.','P04-W011;P04-W012;P04-W034'),
('2024-05-24','environmental_programme','Emotions, climate, and the environment workshop held with CHEP funding.','CHEP; CHSP; Anatole Le Bras','Links environmental, medical and emotions history.','P04-W006;P04-W017'),
('2024-11-06','reading_programme','First announced Climate and Capitalism reading-workshop session.','CHEP; Liane Hewitt; CHSP','Group operation documented retrospectively; specific session occurrence unconfirmed.','P04-N201;P04-N005'),
('2025-06-26','partnership','New Paths in Environmental History workshop held in Paris.','Paris CHEP; Cambridge CHE; Sciences Po','First meeting of an explicitly linked workshop sequence.','P04-W001;P04-W017'),
('2026-06-26','partnership','JCHE/CHEP workshop held with Paris and Cambridge participants.','Paris CHEP; Cambridge CHE','Follow-up exchange; precise venue remains partly inferred.','P04-W001;P04-W002'),
('2026-07-06','thematic_conference','State and Capital conference announced for 6–7 July 2026, co-organised by CHEP.','CHEP; CHSP; CEVIPOF','State/economy programming; programme does not prove occurrence.','P04-W019;P04-W020')]
for i,(d,cat,desc,ent,sig,ids) in enumerate(add,1):
    milestones.append(dict(milestone_id='',date_start=d,date_end='2026-07-07' if d=='2026-07-06' else '2022-11-10' if d=='2022-11-09' else d,date_precision='day_range' if d in ['2026-07-06','2022-11-09'] else 'day',category=cat,description=desc,entities=ent,significance=sig,evidence_status='verified',source_ids=ids,source_record_id=f'P04-RM{i:03d}',as_of_date='2026-11-15'))
# Keep retrospective prehistory first without inventing its date.
milestones.sort(key=lambda m:('0000' if m['category']=='early_network_pre_history' else m['date_start'],m['category']))
for i,m in enumerate(milestones,1):
    m['milestone_id']=f'P04-M{i:03d}'
    ids=m['source_ids'].split(';'); assert all(x in source_by_id for x in ids)
    m['source_urls']=';'.join(dict.fromkeys(source_by_id[x]['url'] for x in ids))
writecsv('timeline.csv',milestones,['milestone_id','date_start','date_end','date_precision','category','description','entities','significance','evidence_status','source_ids','source_record_id','source_urls','as_of_date'])
writecsv('sources.csv',sorted(sources,key=lambda s:s['source_id']),['source_id','url','title','publisher_or_owner','source_date','accessed_at','source_type','supports','retrieval_status'])
main=[e for e in events if e['counted_in_census']=='true']
year=defaultdict(Counter)
for e in main:
    y=e['date_start'][:4] if e['date_start']!='date_unknown' else 'unknown'
    year[y]['records']+=1; year[y][e['status']]+=1
    if e['temporal_scope']=='future': year[y]['future']+=1
yearlines=['| Year | Records | Documented as held | Announced | Status unknown / postponed | Future subset |','|---|---:|---:|---:|---:|---:|']
for y,c in sorted(year.items()): yearlines.append(f"| {y} | {c['records']} | {c['documented as held']} | {c['announced']} | {c['status unknown']+c['cancelled/postponed']} | {c['future']} |")
stats={'event_rows':len(events),'census_records':len(main),'unverified_leads':len(events)-len(main),'future':sum(e['temporal_scope']=='future' for e in main),'statuses':dict(Counter(e['status'] for e in main)),'groups':dict(Counter(e['census_group'] for e in main)),'milestones':len(milestones),'source_rows':len(sources),'source_unique_urls':len(set(s['url'] for s in sources)),'year_table':'\n'.join(yearlines)}
(R/'final_counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
report=(BASE/'report.md').read_text()
for k,v in {'EVENT_COUNT':len(main),'FUTURE_COUNT':stats['future'],'HELD_COUNT':stats['statuses']['documented as held'],'YEAR_TABLE':stats['year_table']}.items(): report=report.replace('{{'+k+'}}',str(v))
(BASE/'report.md').write_text(report)
print(json.dumps(stats,ensure_ascii=False,indent=2))
