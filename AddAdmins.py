import requests
import json
import csv
import config

# Replace the placeholders with your own values
organization_id = config.organization_id
admins_file = config.admins_file
api_key = config.api_key

#api_key = config.api_key Define the API endpoint and headers
endpoint = "https://api.meraki.com/api/v1/organizations/{organization_id}/admins"
headers = {
    "X-Cisco-Meraki-API-Key": api_key,
    "Content-Type": "application/json"
}
# Open the CSV file and read the list of admins
with open(admins_file, "r") as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        # Create a data payload for the new admin
        data = {
            "email": row[0],
            "name": row[1],
            "orgAccess": row[2],
            "tags": row[3].split(",") if row[3] else [],
            "networks": row[4].split(",") if row[4] else []
        }
        # Send the API request to add the admin
        response = requests.post(endpoint.format(organization_id=organization_id), headers=headers, data=json.dumps(data))
        # Check the response status code
        if response.status_code == 201:
            print("Admin '{}' added successfully".format(row[1]))
        else:
            print("Error adding admin '{}': {}".format(row[1], response.text))
