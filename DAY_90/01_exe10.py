# Use the NewsAPI and the requests
# module to fetch the daily news
# related to different topics.
# Go to: https://newsapi.org/
# and explore the various options
# to build you application
# Easy que for me
import requests

API_KEY = "# Replace with your NewsAPI key"  

topic = input("Enter a topic: ")

url = "https://newsapi.org/v2/everything"

params = {
    "q": topic,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 5,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

if data["status"] == "ok":
    print(f"\nTop News on '{topic}':\n")
    
    for i, article in enumerate(data["articles"], start=1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}")
        print()
else:
    print("Error:", data.get("message", "Unknown error"))
