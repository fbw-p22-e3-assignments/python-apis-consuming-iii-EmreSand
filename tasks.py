import requests
# import os
# from dotenv import load_dotenv
import pprint

#load_dotenv()

# # Task 1: GET call to get some companies

# url = "https://fakerapi.it/api/v1/companies?_quantity=20"

# headers = {
#     "content_type": "application/json"

# }
    
# response = requests.get(url, headers=headers)

# pprint.pprint(response.json())

# # Task 2: GET call to get 50 persons with English names who were born after 1994

# url = "https://fakerapi.it/api/v1/persons?_quantity=50&_birthday_start=1994-12-31&_locale=en_EN"

# headers = {
#     "content_type": "application/json"

# }
    
# response = requests.get(url, headers=headers)

# pprint.pprint(response.json())

# # Task 3: GET call to get 5 German companies

# url = "https://fakerapi.it/api/v1/companies?_locale=de_DE&_quantity=5"

# headers = {
#     "content_type": "application/json"

# }
    
# response = requests.get(url, headers=headers)

# pprint.pprint(response.json())

# # Task 4:  GET call to retrieve 60 credit cards of Spanish people.

# url = "https://fakerapi.it/api/v1/credit_cards?_quantity=60&_locale=es_ES"

# headers = {
#     "content_type": "application/json"

# }
    
# response = requests.get(url, headers=headers)

# pprint.pprint(response.json())

# Task 5: GET call to retrieve 47 products that cost higher than 50€

url = "https://fakerapi.it/api/v1/products?_quantity=47&_price_min=50.0"

headers = {
    "content_type": "application/json"

}
    
response = requests.get(url, headers=headers)

pprint.pprint(response.json())

# Task 6: GET call to retrieve 10 Custom objects with "pokemon", "website", and "name" fields

# url = "https://fakerapi.it/api/v1/custom?_quantity=10&customfield1=pokemon&customfield2=website&customfield3=name"

# headers = {
#     "content_type": "application/json"

# }
    
# response = requests.get(url, headers=headers)

# pprint.pprint(response.json())