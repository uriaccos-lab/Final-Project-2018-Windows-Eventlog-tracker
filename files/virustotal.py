#  File size limit is 32MB!
import requests

params = {'apikey': 'c1e5a2ec5a91f6270157e43c0f05ba8cf66a99e419d14707d64dd90b628c4af4'}
files = {'file': ('eclipseuninstall', open('D:\\Program Files (x86)\\eclipse\\uninstall.exe', 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files = files, params=params)
json_response = response.json()
for line in json_response:
    print line, json_response[line]
print json_response['md5']
