# Fog Director RESTful API

CISCO Fog Director delivers the capability to manage large-scale production deployments of IOx-enabled fog applications. 

The RESTful API official documentation is [https://developer.cisco.com/docs/iox/#!fog-director-api-documentation/cisco-fog-director-rest-api](here) but it appears incomplete if compared with the example provided in the [https://github.com/CiscoIOx/Fog-Director-REST-Clients](CiscoIOX REST Clients GitHub Repository).

This fork tries to give to this API a better (and complete) documentation merging the official documentation with the unknown API found in the examples.

# API
 - get_token(ip,username,password)
 - delete_token(ip, token)
 - delete_token(ip, token)
 - add_device(ip, token, device_ip, device_user, device_psw, device_port = 8443)
 - delete_device(ip, token, device_id)
 - get_devices(ip, token, limit = 10000)
 - delete_all_devices(ip,token, limit=10000)
 - add_app(ip, token, app_file)
 - is_app_present(ip, token, app_name)
 - get_all_tags(ip,token)