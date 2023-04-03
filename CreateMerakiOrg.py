import meraki
import config

api_key = config.api_key
dashboard = meraki.DashboardAPI(api_key)

org_name = 'Name'
org_type = 'enterprise'

org = dashboard.organizations.createOrganization(org_name, org_type)
print(f'New organization created with ID {org["id"]}')
