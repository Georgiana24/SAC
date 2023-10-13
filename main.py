from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import random
import pandas as pd

client = RecombeeClient('sac2023-dev', 'aGEP9NP4K3NRZv2TNIC4n6ZIE4yAJSwl6naL4a8IxygygKxEtZx7DAv90RQFELmU')

course_df = pd.read_csv("books.csv")

# Salvarea proprietati produse
""""
client.send(AddItemProperty('isbn', 'string'))
client.send(AddItemProperty('title', 'string'))
client.send(AddItemProperty('authors', 'string'))
client.send(AddItemProperty('original_publication_year', 'string'))
client.send(AddItemProperty('language_code', 'string'))
client.send(AddItemProperty('average_rating', 'string'))
"""

# Salvare valori proprietati produse + upload id-uri produse
requests = [SetItemValues(
    course_df.index[i], #itemId
    #values:
    {
        "isbn": course_df['isbn'][i],
        "title":  course_df['title'][i],
        "authors": course_df['authors'][i],
        "original_publication_year": course_df['original_publication_year'][i],
        "language_code": course_df['language_code'][i],
        "average_rating": course_df['average_rating'][i]
    },
    cascade_create=True

  ) for i in range(len(course_df))]

client.send(Batch(requests))