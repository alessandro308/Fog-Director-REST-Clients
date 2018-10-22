"""
Copyright 2016 Ashok Kanagarsu

These are sample functions for the Cisco Fog Director REST API.


See: 

http://www.cisco.com/c/en/us/td/docs/routers/access/800/software/guides/iox/fog-director/reference-guide/1-0/fog_director_ref_guide.html

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
#from functions import *
import requests
import json
import base64
def get_token(ip,username,password):
    #print(ip)
    url = "https://%s/api/v1/appmgr/tokenservice" % ip
    print(url)

    r = requests.post(url,auth=(username,password),verify=False)
    token=''
    if  r.status_code == 202:
        print(r.json())
        token = r.json()['token']
        #print(token)
    else:
        print("ERROR")
        print "Status code is "+str(r.status_code)
        print r.text
    return(token)

def search_devices_with_tag(ip,token):
    tag_to_search=raw_input("enter the tag to be searched")
    url = "https://%s/api/v1/appmgr/devices?limit=10000&offset=0&searchByTags=%s" % (ip,tag_to_search)
    headers = {'x-token-id':token,'content-type': 'application/json'}
    r=requests.get(url,headers=headers,verify=False)
    print(r.status_code)
    print("devices which are tagged with this specific tag on your  FD")
    devices=json.loads((json.dumps(r.json())))
    if(len(devices['data'])==0):
    	print("there are no devices which are tagged with this tag")
    else:
    	for index in range(len(devices['data'])):
			device_id=devices['data'][index]['deviceId']
			ip_addr=devices['data'][index]['ipAddress']
			print(str(device_id))
			print(str(ip_addr))


def delete_token(ip, token):
    url = "https://%s/api/v1/appmgr/tokenservice/%s" % (ip, token)
  
    headers = {'x-token-id':token,'content-type': 'application/json'}
    
    r = requests.delete(url,headers=headers,verify=False)

    if  r.status_code == 200:
        print(r.json())
    else:
        print("ERROR")
        print "Status code is "+str(r.status_code)
        print r.text    

app_mgr_ip=raw_input("Enter app manager ip address")
username=raw_input("enter the username of your FD:")
password=raw_input("enter the password of your FD:")
print "loging to FD and fetch an TOKEN"
token_id=get_token(app_mgr_ip,username,password)
print "Search device which are tagged with a specific TAG "
search_devices_with_tag(app_mgr_ip,token_id)
print "Logging out of Fog Director"
delete_token(app_mgr_ip, token_id)