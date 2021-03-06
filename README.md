# Fog Director RESTful API

<img src="https://www.cisco.com/content/dam/assets/prod/im/img/600/fog-director-600x400.jpg" width="500px">

CISCO Fog Director delivers the capability to manage large-scale production deployments of IOx-enabled fog applications. 

The RESTful API official documentation is [here](https://developer.cisco.com/docs/iox/#!fog-director-api-documentation/cisco-fog-director-rest-api) but it appears incomplete if compared with the example provided in the CiscoIOX REST Clients [GitHub Repository](https://github.com/CiscoIOx/Fog-Director-REST-Clients).

This fork tries to give to this API a better (and complete) documentation merging the official documentation with the unknown API found in the examples.

# API
### Authentication
 - get_token(ip,username,password)
 - delete_token(ip, token)
### Managing Devices
 - add_device(ip, token, device_ip, device_user, device_psw, device_port = 8443)
 - delete_device(ip, token, device_id)
 - get_devices(ip, token, limit = 10000)
 - delete_all_devices(ip,token, limit=10000)
### Applications
#### LocalApp Endpoint, used to add or upgrade app
 - add_app(ip, token, app_file)
 - get_app_details(ip, token, appname, search_limit=100)
#### Myapp Endpoint, used to manage lifecycle actions for devices
 - get_myapp_details(ip, token, myapp_name)
 - create_myapp(ip, token, appname)
 - is_myapp_present(ip, token, app_name)
 - install_app(ip, token, appname, deviceip, resources=None)
 - uninstall_app(ip, token, appname, deviceip)
 - stop_app(ip, token, appname)
 - start_app(ip, token, appname)
### Tags
 - get_all_tags(ip,token)