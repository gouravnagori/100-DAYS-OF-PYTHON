import requests
response = requests.get("https://opti-meal.vercel.app/")
print(response.text)