import requests
import pprint
import json
params = {'apikey': 'c1e5a2ec5a91f6270157e43c0f05ba8cf66a99e419d14707d64dd90b628c4af4', 'resource': '50d13b93ca49d9d9f0650b3f069a6a8c'}
headers = {"Accept-Encoding": "gzip, deflate", "User-Agent": "gzip, My Python requests library example client or username"}
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
json_response = response.json()   # <type 'dict'>
i=0
if (json_response["positives"]/json_response["total"])*100 > 50:
    print "malware detected"
else:
    print "clean!"
for line in json_response:
    if isinstance(json_response[line], dict):
        print i
        for l in json_response[line]:
            print l, json_response[line][l]
    else:
        print i, line,type(json_response[line]), json_response[line]
    i += 1
