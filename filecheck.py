import json

with open('project.json') as f:
  df = json.load(f)

r = {}
for skey in df['targets'][0]['blocks']:
  k = df['targets'][0]['blocks'][skey]['opcode']
  if k in r:
    r[k] += 1
  else:
    r[k] = 1
print(sorted(r.items(), key=lambda x:x[0]))
