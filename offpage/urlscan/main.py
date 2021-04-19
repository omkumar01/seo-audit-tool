import requests
import json
from keys import headers
from result import exData

data = {"url": "https://heapoftech.live/", "visibility": "public"}

response = requests.post(
    "https://urlscan.io/api/v1/scan/", headers=headers, data=json.dumps(data)
)

print(response)

print(exData(response.json()))