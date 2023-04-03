import meraki
import config

# Initialize the client
client = meraki.DashboardAPI(api_key=config.api_key)

# Call the API to get the list of organizations
orgs = client.organizations.getOrganizations()
print(orgs)
#{'id': '601230550253961288', 'name': 'Southeast Neighborhood Development', 'url': 'https://n68.meraki.com/o/V_oAVbeb/manage/organization/overview', 'api': {'enabled': True}, 'licensing': {'model': 'co-term'}, 'cloud': {'region': {'name': 'North America'}}

# Print the list of organizations
for org in orgs:
    print(f'Name: {org["name"]}, ID: {org["id"]}')
