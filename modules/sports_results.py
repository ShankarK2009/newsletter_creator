import requests
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()

soccer = []
bball = []
madness = []

def sports(num):
    params = {
    "q": "premier league past matches",
    "location": "austin, texas, united states",
    "api_key": os.getenv("SERP_API")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results["sports_results"])
    sports_results = results["sports_results"]

    games = sports_results["games"]
    
    print("\nMatch Summary for Premier League")
    print("=" * 40)
    for game in games[:num]:
        print(game["teams"][0]["name"])
        print(game["teams"][0]["thumbnail"])
        print(game["teams"][0].get("score", "N/A"))
        print("-"*10)
        print(game["teams"][1]["name"])
        print(game["teams"][1]["thumbnail"])
        print(game["teams"][1].get("score", "N/A"))
        soccer.append([game["teams"][0]["name"], game["teams"][1]["name"], game["teams"][0]["thumbnail"], game["teams"][1]["thumbnail"], game["teams"][0].get("score", "N/A"), game["teams"][1].get("score", "N/A")])
    print("=" * 40)



    #SOCCER LA LIGA
    params = {
    "q": "la liga past matches",
    "location": "austin, texas, united states",
    "api_key": os.getenv("SERP_API")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results["sports_results"])
    sports_results = results["sports_results"]

    games = sports_results["games"]
    
    print("\nMatch Summary for La Liga")
    print("=" * 40)
    for game in games[:num]:
        print(game["teams"][0]["name"])
        print(game["teams"][0]["thumbnail"])
        print(game["teams"][0].get("score", "N/A"))
        print("-"*10)
        print(game["teams"][1]["name"])
        print(game["teams"][1]["thumbnail"])
        print(game["teams"][1].get("score", "N/A"))
        soccer.append([game["teams"][0]["name"], game["teams"][1]["name"], game["teams"][0]["thumbnail"], game["teams"][1]["thumbnail"], game["teams"][0].get("score", "N/A"), game["teams"][1].get("score", "N/A")])
    print("=" * 40)


    #UCL
    params = {
    "q": "ucl matches",
    "location": "austin, texas, united states",
    "api_key": os.getenv("SERP_API")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    sports_results = results["sports_results"]

    games = sports_results["games"]
    
    print("\nMatch Summary for UCL")
    print("=" * 40)
    for game in games[:num]:
        print(game["teams"][0]["name"])
        print(game["teams"][0]["thumbnail"])
        print(game["teams"][0].get("score", "N/A"))
        print("-"*10)
        print(game["teams"][1]["name"])
        print(game["teams"][1]["thumbnail"])
        print(game["teams"][1].get("score", "N/A"))
        soccer.append([game["teams"][0]["name"], game["teams"][1]["name"], game["teams"][0]["thumbnail"], game["teams"][1]["thumbnail"], game["teams"][0].get("score", "N/A"), game["teams"][1].get("score", "N/A")])
    print("=" * 40)


    #NBA
    params = {
    "q": "nba past matches",
    "location": "austin, texas, united states",
    "api_key": os.getenv("SERP_API")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    sports_results = results["sports_results"]

    games = sports_results["games"]
    
    print("\nMatch Summary for NBA")
    print("=" * 40)
    for game in games:
        print(game["teams"][0]["name"])
        print(game["teams"][0]["thumbnail"])
        print(game["teams"][0].get("score", "N/A"))
        print("-"*10)
        print(game["teams"][1]["name"])
        print(game["teams"][1]["thumbnail"])
        print(game["teams"][1].get("score", "N/A"))
        bball.append([game["teams"][0]["name"], game["teams"][1]["name"], game["teams"][0]["thumbnail"], game["teams"][1]["thumbnail"], game["teams"][0].get("score", "N/A"), game["teams"][1].get("score", "N/A")])
    print("=" * 40)


    #March Madness
    params = {
    "q": "march madness past matches",
    "location": "austin, texas, united states",
    "api_key": os.getenv("SERP_API")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    sports_results = results["sports_results"]

    games = sports_results["games"]
    
    print("\nMatch Summary for March Madness")
    print("=" * 40)
    for game in games:
        print(game["teams"][0]["name"])
        print(game["teams"][0]["thumbnail"])
        print(game["teams"][0].get("score", "N/A"))
        print("-"*10)
        print(game["teams"][1]["name"])
        print(game["teams"][1]["thumbnail"])
        print(game["teams"][1].get("score", "N/A"))
        madness.append([game["teams"][0]["name"], game["teams"][1]["name"], game["teams"][0]["thumbnail"], game["teams"][1]["thumbnail"], game["teams"][0].get("score", "N/A"), game["teams"][1].get("score", "N/A")])
    print("=" * 40)

    # #NFL (Not season yet)
    # game = requests.post("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard")
    # game = game.json()
    # for match in data["events"]:
    #     # Extract game state
    #     status = match['competitions'][0]['status']['type']
    #     state = status['state']  # "pre", "in", or "post"
    #     state_description = status['description']  # e.g., "Scheduled", "In Progress", "Final"

    #     print(f"Date: {match['date']}")
    #     print(f"Teams: {match['competitions'][0]['competitors'][0]['team']['name']} vs {match['competitions'][0]['competitors'][1]['team']['name']}")
    #     print(f"Score: {match['competitions'][0]['competitors'][0]['score']} - {match['competitions'][0]['competitors'][1]['score']}")
    #     print(f"State: {state_description}")

    #     # Initialize lists to store top performers
    #     passing_leaders = []
    #     rushing_leaders = []
    #     receiving_leaders = []

    #     # Loop through leaders to find top performers
    #     for leader in match['competitions'][0]['leaders']:
    #         if leader['name'] == 'passingYards':
    #             for performer in leader['leaders']:
    #                 passing_leaders.append(f"{performer['athlete']['displayName']} ({performer['displayValue']})")
    #         elif leader['name'] == 'rushingYards':
    #             for performer in leader['leaders']:
    #                 rushing_leaders.append(f"{performer['athlete']['displayName']} ({performer['displayValue']})")
    #         elif leader['name'] == 'receivingYards':
    #             for performer in leader['leaders']:
    #                 receiving_leaders.append(f"{performer['athlete']['displayName']} ({performer['displayValue']})")

    #     # Print top performers if any
    #     if passing_leaders:
    #         print("Passing Leader:")
    #         for performer in passing_leaders:
    #             print(f"  - {performer}")
    #     else:
    #         print("Passing Leader: None")

    #     if rushing_leaders:
    #         print("Rushing Leader:")
    #         for performer in rushing_leaders:
    #             print(f"  - {performer}")
    #     else:
    #         print("Rushing Leader: None")

    #     if receiving_leaders:
    #         print("Receiving Leader:")
    #         for performer in receiving_leaders:
    #             print(f"  - {performer}")
    #     else:
    #         print("Receiving Leader: None")

    #     print("-" * 40)
    # print("=" * 40)
    print("End of Sports")
    return soccer, bball, madness