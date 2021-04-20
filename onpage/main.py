import requests
from bs4 import BeautifulSoup
from headers import headerCount
from title import titleText
from meta import metaTags
from schema import checkSchema

url = "https://www.udemy.com/"


html = requests.get(url)
page = BeautifulSoup(html.content, "html.parser")

# print(type(page))
# print(headerCount(page))

# print(titleText(page))
# print(metaTags(page))
print(checkSchema(page))