import requests
import config



dict = {}
dict['name']= 'shashwat'
dict['email']= 'kotiyalsha@gmail.com'
dict['status']= 'status'
dict['gender']= 'male'


print(dict)
url =config.users()
r = requests.post(url,data=dict)
print(r.status_code)
header = {}
token=config.get_apikey()
print(token)
header['Authorization']= 'Bearer' + token
r = requests.post(url, data=dict, headers=header)
print(r.status_code)