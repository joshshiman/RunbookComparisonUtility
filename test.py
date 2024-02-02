import requests
from bs4 import BeautifulSoup

URL = "https://github.com/IBM/itz-support-public/tree/main/IBM-Technology-Zone/IBM-Technology-Zone-Runbooks"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all(class_="Link--primary")

print(page.text)