import requests
import json

# Set the API endpoint URLs
get_settings_url = "https://api.meraki.com/api/v1/networks/{networkId}/syslogServers"
update_settings_url = "https://api.meraki.com/api/v1/networks/{networkId}/syslogServers"

# Set the request headers and body
headers = {
    "X-Cisco-Meraki-API-Key": "{apiKey}",
    "Content-Type": "application/json"
}
body = {
    "event_logs_enabled": True,
    "event_logs_destinations": [
        {
            "ip": "192.0.2.1",
            "port": 514,
            "roles": ["network_admin", "helpdesk"]
        }
    ]
}

# Set the network ID
networkId = "networkId"

# Insert the network ID into the URLs
get_settings_url = get_settings_url.format(networkId=networkId)
update_settings_url = update_settings_url.format(networkId=networkId)

# Get the current network settings
response = requests.get(get_settings_url, headers=headers)

# Check the response status code
if response.status_code != 200:
    print("Error getting network settings")
    exit()

# Parse the response JSON and update the logging settings
settings = response.json()
settings["event_logs_enabled"] = body["event_logs_enabled"]
settings["event_logs_destinations"] = body["event_logs_destinations"]

# Update the network settings
response = requests.put(update_settings_url, headers=headers, data=json.dumps(settings))

# Check the response status code
if response.status_code == 200:
    print("General settings updated successfully")
else:
    print("Error updating general settings")
