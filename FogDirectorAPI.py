import requests
import json
import base64

# Suppressing all warning given by the unverified HTTPS requestes
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token(ip,username,password):
    url = "https://%s/api/v1/appmgr/tokenservice" % ip
    r = requests.post(url,auth=(username,password),verify=False)
    token=''
    if  r.status_code == 202:
        token = r.json()['token']
    else:
        print("ERROR")
        print "Status code is "+str(r.status_code)
        print r.text
    return(token)

def delete_token(ip, token):
    url = "https://%s/api/v1/appmgr/tokenservice/%s" % (ip, token)
    headers = {'x-token-id':token,'content-type': 'application/json'}
    r = requests.delete(url,headers=headers,verify=False)
    if  r.status_code != 200:
        raise SystemError(r.raise_for_status())

def add_device(ip, token, device_ip, device_user, device_psw, device_port = 8443):
    url = "https://%s/api/v1/appmgr/devices" % ip
    headers = {'x-token-id':token,'content-type': 'application/json'}
    data = {'port':device_port,'ipAddress':device_ip,'username':device_user,'password':device_psw}
    r = requests.post(url,data=json.dumps(data),headers=headers,verify=False)
    if r.status_code!=201:
        raise SystemError(r.raise_for_status())

def delete_device(ip, token, device_id):
    headers = {'x-token-id':token,'content-type': 'application/json'}
    url = "https://%s/api/v1/appmgr/devices/%s" % (ip, str(device_id))
    r=requests.delete(url, headers=headers, verify=False)
    if r.status_code != 200:
        raise SystemError(r.raise_for_status())

"""
    Returns a JSON
    { 
        data: [
            {
                "availableSerialDevices": [],
                "status": string,
                "supportedFeature":[strings],
                "supportedResourceProfiles": [{ 
                    name:{
                        "vCPU": integer,
                        "cpuShare": integer,
                        "memoryShare": integer
                    }
                }],
                "usedUsbDevices":[ ],
                "usedSerialDevices":[ ],
                "port":integer,
                "capability":{  
                    "nodes":[
                        {  
                            "name":"x86_64",
                            "maxVCPUPerApp":2,
                            "totalVCPU":2,
                            "cartridges":[],
                            "memory":{  
                                "available":1381,
                                "total":1637
                            },
                            "disk":{  
                                "available":812,
                                "total":822
                            },
                            "cpu":{  
                                "available":1143,
                                "total":1743
                            }
                        }
                        ],
                        "supportedApps":[  "DOCKER", "PAAS", "LXC" ],
                        "managementAPIVersion":"2.0"
                    },
                    "hostname":"iox-caf-1",
                    "apps":[  

                    ],
                    "networks":[  
                        {  
                        "networkDescription":{  
                            "repofolder":"/software/caf/work/network",
                            "ip_end":null,
                            "name":"iox-bridge0",
                            "mirror_mode":false,
                            "private_route_table":"10",
                            "source_linux_bridge":"svcbr_0",
                            "subnet_mask":null,
                            "gateway_ip":null,
                            "app_ip_map":{  

                            },
                            "external_interface":"VPG0",
                            "network_type":"bridge",
                            "ip_start":null,
                            "description":" - bridge"
                        },
                        "networkName":"iox-bridge0"
                        },
                        {  
                        "networkDescription":{  
                            "repofolder":"/software/caf/work/network",
                            "ip_end":"192.168.10.30",
                            "name":"iox-nat0",
                            "mirror_mode":false,
                            "private_route_table":"10",
                            "source_linux_bridge":"svcbr_0",
                            "subnet_mask":"255.255.255.224",
                            "gateway_ip":"192.168.10.1",
                            "nat_range_cidr":"192.168.10.0/27",
                            "app_ip_map":{  

                            },
                            "external_interface":"VPG0",
                            "network_type":"nat",
                            "ip_start":"192.168.10.2",
                            "description":" - nat"
                        },
                        "networkName":"iox-nat0"
                        }
                    ],
                    "readonly":false,
                    "_links":{  
                        "self":{  
                        "href":"/api/v1/appmgr/devices/6769006a-a0d9-4922-b682-5a5283aba9da"
                        },
                        "apps":{  
                        "href":"/api/v1/appmgr/devices/6769006a-a0d9-4922-b682-5a5283aba9da/apps"
                        },
                        "logs":{  
                        "href":"/api/v1/appmgr/devices/6769006a-a0d9-4922-b682-5a5283aba9da/logs"
                        },
                        "techsupport":{  
                        "href":"/api/v1/appmgr/devices/6769006a-a0d9-4922-b682-5a5283aba9da/techsupport"
                        }
                    },
                    "ne_id":"10.10.20.51:8443",
                    "userProvidedSerialNumber":"",
                    "username":"cisco",
                    "description":{  
                        "content":"",
                        "contentType":"text"
                    },
                    "tags":[  
                        {  
                        "tagId":"2714",
                        "name":"httpd",
                        "description":""
                        }
                    ],
                    "errorMessage":"",
                    "platformVersionDetails":{  
                        "caf_version_info":{  
                        "build_number":7,
                        "branch":"r/1.7.0.0",
                        "revision":"0866bf2f310712517dea4a9df2e9030f8e0b1286"
                        },
                        "platform_version_info":{  

                        },
                        "caf_version_name":"ARYABHATTA",
                        "platform_version_number":"0",
                        "repo":{  
                        "supported_versions":[  
                            "1.0"
                        ],
                        "repo_version":"1.0"
                        },
                        "caf_version_number":"1.7.0.7"
                    },
                    "deviceId":"6769006a-a0d9-4922-b682-5a5283aba9da",
                    "platformVersion":"1.7.0.7",
                    "useLocalImages":false,
                    "availableUsbDevices":[  

                    ],
                    "ipv6Supported":false,
                    "lostContact":false,
                    "serialNumber":"UCS3e731b85-35ca-4960-9cf2-5fe244262227",
                    "contactDetails":"",
                    "lastHeardTime":1540222574081,
                    "ipAddress":"10.10.20.51"
                },
                ...
            }
        ]

    }
"""
def get_devices(ip, token, limit = 10000):
    url = "https://%s/api/v1/appmgr/devices?offset=0&limit=%d" % (ip, limit)
    headers = {'x-token-id':token,'content-type': 'application/json'}
    r=requests.get(url,headers=headers,verify=False)
    return json.loads((json.dumps(r.json())))

def delete_all_devices(ip,token, limit=10000):
    devices=get_devices(ip, token)
    for index in range(len(devices['data'])):
        device_id=devices['data'][index]['deviceId']
        delete_device(ip, token, device_id)

def add_app(ip, token, app_file):
    url = "https://%s/api/v1/appmgr/localapps/upload" % ip
    headers = {'x-token-id':token}
    r = requests.post(url, headers=headers, files={'file': open(app_file,'rb')}, verify=False)                      
    if  r.status_code != 201:
        raise SystemError(r.raise_for_status())

def is_app_present(ip, token, app_name):
    url = "https://%s/api/v1/appmgr/myapps?searchByName=%s" % (ip, app_name)
    headers = {'x-token-id':token,'content-type': 'application/json'}
    r=requests.get(url,headers=headers,verify=False)
    if r.text=='{}' :
        return False
    else :
        return True

# Returns all the tags from apps
def get_all_tags(ip,token):
    url="https://%s/api/v1/appmgr/tags/" % ip
    headers = {'x-token-id':token,'content-type': 'application/json'}
    r=requests.get(url,headers=headers,verify=False)
    tags= json.loads((json.dumps(r.json())))
    result = []
    for index in range(len(tags['data'])):
        tag_id=tags['data'][index]['tagId']
        tag_name=tags['data'][index]['name']
        result.append((tag_id, tag_name))

ip = "10.10.20.50"
token = get_token(ip, "admin", "admin_123")
print get_all_tags(ip, token)