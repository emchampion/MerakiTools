import meraki
import config

client = meraki.DashboardAPI(api_key=config.api_key)

org_id = input("Enter the org ID: ")

networks = client.organizations.getOrganizationNetworks(org_id)

for network in networks:
    print(network['name'], network['id'])