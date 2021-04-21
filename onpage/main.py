import requests
from bs4 import BeautifulSoup
from headers import headerCount
from title import titleText
from meta import metaTags
from schema import checkSchema
from lang import getLang
from imgdata import imgAlt

url = "https://heapoftech.live/"


html = requests.get(url)
page = BeautifulSoup(html.content, "html.parser")

# print(type(page))
# print(headerCount(page))

# print(titleText(page))
# print(metaTags(page))
# print(checkSchema(page))

# print(getLang(page))

# print(imgAlt(page))