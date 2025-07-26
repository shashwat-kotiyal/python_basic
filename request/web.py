import requests


r = requests.get("https://pypi.org/project/requests/")

print(r.status_code)
print(r.ok)
# print(r.headers)
#print(r.content)

payload={'page':2 ,'count':25}
r =requests.get("https://httpbin.org/#/", params=payload)
print(r.url)

print(r.text)

payload ={'username':'shahswat', 'password':'skotiyal'}
r =requests.post("https://httpbin.org/#/post", data=payload)
print(r.json())