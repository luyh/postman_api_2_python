import requests
import json

url = "https://www.okcoin.com/api/v1/ticker.do"

querystring = {"symbol":"btc_usd"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "571019e9-2394-b4f8-6da6-374fafa72377"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
print(type(response.text))


#####


r = response.json()
print(r)
print(type(r))

print(r['date'])
