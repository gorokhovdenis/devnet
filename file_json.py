import json
import re

with open('data.json') as json_file:
    data=json.load(json_file)
    print data['queryResponse']["entity"][0]["devicesDTO"]['ipAddress']
#    for p in data['queryResponse']
#        print(p['ipAddress'])

   # for i in data:
    #    if data[i] == 'devicesDTO':
     #      print data[i]
#with open('data.json') as f:
#    content = f.read()
#    print content
#    print len(set(m.group(1) for m in re.finditer('"deviceType": (\d+)', content)))

