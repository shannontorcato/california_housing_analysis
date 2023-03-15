import requests

url = "https://soccer.sportmonks.com/api/v2.0/fixtures/16475287"

payload={}
headers = {

}

response = requests.request("GET", url, headers=headers, data=payload)

print('Hello')
print(response.text)