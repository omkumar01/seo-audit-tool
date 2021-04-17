import requests
from bs4 import BeautifulSoup
from headers import headerCount

url = "https://heapoftech.live"


html = requests.get(url)
page = BeautifulSoup(html.content, "html.parser")


print(headerCount(page))
