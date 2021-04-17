import requests
import json

key = "JRRI6QCDQCP5FZQBNRJKZTJWNXY8ZCSC"
domain = "heapoftech.live"

response = requests.get(f"https://api.ip2whois.com/v1?key={key}&domain={domain}")

print(response.json())