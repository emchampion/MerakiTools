import requests
import config

# Set your Meraki API key
API_KEY = config.api_key

# Set the device MAC address you want to search for
device_mac = "10:62:e5:14:9a:88"

# Make a request to the Meraki API to get a list of all organizations
org_url = "https://api.meraki.com/api/v1/organizations"
headers = {"X-Cisco-Meraki-API-Key": API_KEY}
response = requests.get(org_url, headers=headers)
orgs = response.json()

# Loop through all organizations and check if the device MAC is in any of their networks
for org in orgs:
    org_id = org["id"]
    network_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"
    response = requests.get(network_url, headers=headers)
    networks = response.json()
    
    for network in networks:
        network_id = network["id"]
        device_url = f"https://api.meraki.com/api/v1/networks/{network_id}/devices"
        response = requests.get(device_url, headers=headers)
        devices = response.json()
        
        for device in devices:
            if device["mac"] == device_mac:
                print(f"The device with MAC address {device_mac} is located in the network {network['name']} in the organization {org['name']}.")
