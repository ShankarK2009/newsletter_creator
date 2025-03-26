from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

results = []

def get_headlines():
    newsapi = NewsApiClient(api_key=os.getenv("NEWS_API"))

    response = newsapi.get_top_headlines(
                                            language='en',
                                            page_size=4
                                            )
    articles = response['articles']

    for source in articles[:4]:
        print("=" * 40)
        print(f"Title: {source["title"]}")
        print(f"Description: {source["description"]}")
        print(f"Url: {source["url"]}")
        print(f"Image Url: {source["urlToImage"]}")
        print(f"Date: {source["publishedAt"][:source["publishedAt"].find("T")]}")
        print("=" * 40)
        print("\n")
        if source['description'] != None and len(source['description']) > 150:
            results.append([source["urlToImage"], source["title"], source["description"][:130]+"...", source["url"]])
        else:
            results.append([source["urlToImage"], source["title"], source["description"], source["url"]])
    
    return results