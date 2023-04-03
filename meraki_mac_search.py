import requests
import config

# Set up Meraki API key and base URL
api_key = config.api_key
base_url = 'https://api.meraki.com/api/v1'

# Define MAC address to search for
mac_address = input("MAC Address: example e0:63:da:58:2c:9f  ")

# Get list of organizations
headers = {'X-Cisco-Meraki-API-Key': api_key}
response = requests.get(f'{base_url}/organizations', headers=headers)
organizations = response.json()

# Iterate through organizations
for org in organizations:
    org_id = org['id']
    org_name = org['name']
    
    # Get list of networks in organization
    response = requests.get(f'{base_url}/organizations/{org_id}/networks', headers=headers)
    networks = response.json()
    
    # Iterate through networks
    for network in networks:
        network_id = network['id']
        network_name = network['name']
        
        # Get list of devices in network
        response = requests.get(f'{base_url}/networks/{network_id}/devices', headers=headers)
        devices = response.json()
        
        # Iterate through devices
        for device in devices:
            if device['mac'] == mac_address:
                print(f"Device with MAC address {mac_address} found in organization {org_name} and network {network_name}.")