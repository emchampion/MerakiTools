import meraki
import config

# Initialize the client
client = meraki.DashboardAPI(api_key=config.api_key)

# Call the API to get the list of organizations
orgs = client.organizations.getOrganizations()
#this is the pure json output, using for testing
#print(orgs)

# Print the list of organizations Will use the raw JSON in the future
for org in orgs:
    print(f'Name: {org["name"]}, ID: {org["id"]}')
