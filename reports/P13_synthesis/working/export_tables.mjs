import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook} from '@oai/artifact-tool';

const work = path.dirname(fileURLToPath(import.meta.url));
const out = path.dirname(work);
const tables = JSON.parse(await fs.readFile(path.join(work,'tables.json'),'utf8'));
const quote = value => {
  const s = String(value ?? 'not_found_publicly');
  return /[",\r\n]/.test(s) ? '"'+s.replaceAll('"','""')+'"' : s;
};
const results=[];
for (const [name,data] of Object.entries(tables)) {
  const wb=Workbook.create();
  const sheet=wb.worksheets.add('Data');
  const matrix=[data.columns,...data.rows];
  const range=sheet.getRangeByIndexes(0,0,matrix.length,data.columns.length);
  range.values=matrix;
  wb.recalculate();
  const stored=range.values;
  if (JSON.stringify(stored)!==JSON.stringify(matrix)) throw new Error('Value roundtrip mismatch: '+name);
  const inspected=await wb.inspect({kind:'region',sheetId:'Data',range:'A1:D3',maxChars:800,tableMaxRows:3,tableMaxCols:4});
  await fs.writeFile(path.join(out,name),stored.map(row=>row.map(quote).join(',')).join('\r\n')+'\r\n','utf8');
  results.push({file:name,rows:data.rows.length,columns:data.columns.length,roundtrip:'passed'});
}
await fs.writeFile(path.join(work,'table_validation.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify(results));
