import requests
from bs4 import BeautifulSoup as bs
response = requests.get("https://opti-meal.vercel.app/")
# print(response.text)

soup = bs(response.text,'html.parser')

for heading in soup.find_all("p"):
    print(heading.text)


    