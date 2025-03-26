import requests

results = []

def get_headlines():
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=c89e3820dbd34bb1afe2b101c5ecc6a8')
    response = requests.get(url)
    response = response.json()
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