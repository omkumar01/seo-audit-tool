import requests

params = {"capture_full_page": "False", "width": 1920, "height": 1080}

url = "https://heapoftech.live"
response = requests.get(
    f"https://screenshot.abstractapi.com/v1/?api_key=ba5121e7767b40cfa23a1c8d5f7d81c7&url={url}",
    params=params,
)
print(response)

img = response.content

f = open("mobile.jpeg", "wb")
f.write(img)
