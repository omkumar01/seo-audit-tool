import requests
import json
from results import exSSL

url = "https://ssl-certificate-checker.p.rapidapi.com/ssl-certificate"

payload = {
    "url": "https://internship.aicte-india.org/",
}

headers = {
    "content-type": "application/json",
    "x-rapidapi-key": "3d4810694emsh4a550f70014f758p10e1fejsn122215658f85",
    "x-rapidapi-host": "ssl-certificate-checker.p.rapidapi.com",
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response)
page = response.json()

ssldata = exSSL(page)
print(ssldata)
# f = open("response_sample.json", "wb")
# f.write(response.content)
# f.close()