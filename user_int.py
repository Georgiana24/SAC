from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *

client = RecombeeClient('sac2023-dev', 'aGEP9NP4K3NRZv2TNIC4n6ZIE4yAJSwl6naL4a8IxygygKxEtZx7DAv90RQFELmU')

client.send(AddDetailView("User1", "0", cascade_create=True))
client.send(AddDetailView("User2", "0", cascade_create=True))
client.send(AddDetailView("User2", "3", cascade_create=True))
client.send(AddDetailView("User3", "0", cascade_create=True))
client.send(AddDetailView("User3", "5", cascade_create=True))
client.send(AddDetailView("User3", "10", cascade_create=True))
client.send(AddDetailView("User4", "5", cascade_create=True))
client.send(AddDetailView("User4", "20", cascade_create=True))
client.send(AddDetailView("User5", "5", cascade_create=True))
client.send(AddDetailView("User5", "20", cascade_create=True))
client.send(AddDetailView("User6", "3", cascade_create=True))
client.send(AddDetailView("User6", "100", cascade_create=True))

"""
client.send(DeleteUser("User1"))
client.send(DeleteUser("User2"))
client.send(DeleteUser("User3"))
client.send(DeleteUser("User4"))
client.send(DeleteUser("User5"))
client.send(DeleteUser("User6"))
"""