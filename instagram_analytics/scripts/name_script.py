import json

json_data=open('nationalparkservice.json').read()
data=json.loads(json_data)

for x in data:
    x['account_name'] = 'nationparkservice'
with open('newfilenational.json', 'w') as f:
    f.write(json.dumps(data))


