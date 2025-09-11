import os
from dotenv import load_dotenv
load_dotenv(override=True)
api_key = os.getenv('API_KEY')
print(api_key[:5])
BASE_URL = 'https://gorest.co.in/'
BASE_PATH = 'public/'
BASE_VERSION = 'v2/'


USERS= 'users'
#https://gorest.co.in/public/v2/users


def users():
    return BASE_URL + BASE_PATH + BASE_VERSION + USERS

def access_token():
    return os.getenv('TEST_TOKEN')

def get_apikey():
    load_dotenv(override=True)
    return os.getenv('API_KEY')


# pm.request.addHeader(
#     {
#         "key" : "Authorization",
#         "value" : "Bearer e104e77c95988ccb4a2382beb1673ad4fe61f0147a6f6d779f13ed1970c2485c"
#     }
# )