import requests
import config


url = config.users()
print(url)
r = requests.get(url)
print(r)
print(r.text)
print(r.json())
print(r.content)


filter_param={
    "limit" : 5,
    "offset" : 1
}

cookie_data={
    "uid" : 1
}
import json
response =requests.get("https://www.google.com/")
print(response.status_code)
#print(response.json())
print(json.dumps(dict(response.cookies)))


#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

url = "https://api.openweathermap.org/data/2.5/weather"
api_key_weather="d13f6b55721b826a3a415ab4726a2ff3"

queries = {
    "q": input("Enter city name:"),
    "appid" : api_key_weather
}

r = requests.get(url,params=queries)
print(f"Temprature :" + str(round(r.json()['main']['temp'] -273.15, 2)))


#response = requests.get()

