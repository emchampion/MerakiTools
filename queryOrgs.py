import meraki
import config

# Initialize the client
client = meraki.DashboardAPI(api_key=config.api_key)

# Call the API to get the list of organizations
orgs = client.organizations.getOrganizations()

# Print the list of organizations
for org in orgs:
    print(f'Name: {org["name"]}, ID: {org["id"]}')
