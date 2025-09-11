import requests
import config

# r = requests.get("https://pypi.org/project/requests/")
#
# print(r.status_code)
# print(r.ok)
# # print(r.headers)
# #print(r.content)
#
# payload={'page':2 ,'count':25}
# r =requests.get("https://httpbin.org/#/", params=payload)
# print(r.url)
#
# print(r.text)
#
# payload ={'username':'shahswat', 'password':'skotiyal'}
# r =requests.post("https://httpbin.org/#/post", data=payload)
# #print(r.json())

def get1():
    from requests.exceptions import Timeout
    try:
        BASE_URL = "https://www.sharetechnote.com/"
        response = requests.get(BASE_URL,timeout=2)
        #if we want to complete api in 2 sec-> set timeout

        print("Final URL:", response.url)  # Shows the encoded URL
        print("Status Code:", response.status_code)
        print("Body:", response.text)
    except Timeout as to:
        print("timeout error")

        # url = "https://gorest.co.in/"
        # #payload = {"ram": 2, "archit": 5}
        # res = requests.get(url)
        # print(res.status_code)

def retry_get():
    from requests.exceptions import Timeout
    BASE_URL = "https://www.sharetechnote.com/"
    MAX_RETRIES =3
    for _ in range(MAX_RETRIES):
        try:
            res = requests.get(BASE_URL,timeout=0.2)
            print(res.text)
            print(res.status_code)
            break;
        except Timeout as t:
            print("timeout")
    else:
        print("all retries failed")

#print(config.access_token())

if __name__ == "__main__":
#    get1()
#caa023eb88bb07a745876f6edc94ae91cc667afe0e6505beef52a2f254ed8e87
#https://gorest.co.in/
#get with retries
   # retry_get()

    print(config.access_token())
    print(config.get_apikey())