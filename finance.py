from newsapi import NewsApiClient

fin_results = []

def finance():
    newsapi = NewsApiClient(api_key='c89e3820dbd34bb1afe2b101c5ecc6a8')

    top_headlines = newsapi.get_top_headlines(q='',
                                            category='business',
                                            language='en',
                                            page_size=4
                                            )

    # print(top_headlines)

    articles = top_headlines['articles']

    for source in articles:
        print("=" * 40)
        print(f"Title: {source["title"]}")
        print(f"Description: {source["description"]}")
        print(f"Url: {source["url"]}")
        print(f"Image Url: {source["urlToImage"]}")
        print(f"Date: {source["publishedAt"][:source["publishedAt"].find("T")]}")
        print("=" * 40)
        print("\n")
        if len(source['description']) > 150:
            fin_results.append([source["urlToImage"], source["title"], source["description"][:130]+"...", source["url"]])
        else:
            fin_results.append([source["urlToImage"], source["title"], source["description"], source["url"]])
        
    return fin_results


finance()

