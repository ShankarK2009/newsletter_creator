import requests
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API = os.getenv("NEWS_API")

results = []

def get_headlines(num):
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey='+NEWS_API)
    response = requests.get(url)
    response = response.json()
    articles = response['articles']

    print("Headlines")
    for source in articles[:num]:
        print("=" * 40)
        print(f"Title: {source["title"]}")
        print(f"Description: {source["description"]}")
        print(f"Url: {source["url"]}")
        print(f"Image Url: {source["urlToImage"]}")
        print(f"Date: {source["publishedAt"][:source["publishedAt"].find("T")]}")
        print("=" * 40)
        print("\n")
        if source['description'] != None and len(source['description']) > 130:
            results.append([source["urlToImage"], source["title"], source["description"][:130]+"...", source["url"]])
        else:
            results.append([source["urlToImage"], source["title"], source["description"], source["url"]])
    print("End of Headlines")
    return results