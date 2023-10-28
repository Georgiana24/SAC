from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *

client = RecombeeClient('sac2023-dev', 'aGEP9NP4K3NRZv2TNIC4n6ZIE4yAJSwl6naL4a8IxygygKxEtZx7DAv90RQFELmU')

recommended1 = client.send(RecommendItemsToUser('User1', 5))
recommended2 = client.send(RecommendItemsToUser('User2', 5))
recommended3 = client.send(RecommendItemsToUser('User3', 5))
recommended4 = client.send(RecommendItemsToUser('User4', 5))
recommended5 = client.send(RecommendItemsToUser('User5', 5))
recommended6 = client.send(RecommendItemsToUser('User6', 5))

print(recommended1)
print(recommended2)
print(recommended3)
print(recommended4)
print(recommended5)
print(recommended6)