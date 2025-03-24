import requests

soccer = []
bball = []
madness = []

def sports():
    #SOCCER PREM LEAGUE
    data = requests.post("https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard")
    data = data.json()
    print("\nMatch Summary for Premier League")
    print("=" * 40)
    for match in data["events"]:
            print(f"Date: {match['date'][:match['date'].find('T')]}")
            print(f"Teams: {match['competitions'][0]['competitors'][0]['team']['name']} vs {match['competitions'][0]['competitors'][1]['team']['name']}")
            print(f"Team 1 Logo: {match['competitions'][0]['competitors'][0]['team']['logo']}")
            print(f"Team 2 Logo:  {match['competitions'][0]['competitors'][1]['team']['logo']}")
            print(f"Score: {match['competitions'][0]['competitors'][0]['score']} - {match['competitions'][0]['competitors'][1]['score']}")
            print(f"Status: {match['competitions'][0]['status']['type']['description']}")

            soccer.append([match['competitions'][0]['competitors'][0]['team']['shortDisplayName'], match['competitions'][0]['competitors'][1]['team']['shortDisplayName'], match['competitions'][0]['competitors'][0]['team']['logo'], match['competitions'][0]['competitors'][1]['team']['logo'], match['competitions'][0]['competitors'][0]['score'], match['competitions'][0]['competitors'][1]['score'], match['competitions'][0]['status']['type']['description']])

            scorers = []
        
            # Loop through details to find goals
            for detail in match['competitions'][0]['details']:
                if detail['type']['id'] == "70":  # Check if it's a goal
                    for athlete in detail['athletesInvolved']:
                        scorers.append(f"{athlete['displayName']} ({detail['clock']['displayValue']})")
            
            # Print scorers if any
            if scorers:
                print("Scorers:")
                for scorer in scorers:
                    print(f"  - {scorer}")
            else:
                print("Scorers: None")
            
            print("-" * 40)
    print("=" * 40)



    #SOCCER LA LIGA
    data = requests.post("https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard")
    data = data.json()
    print("\nMatch Summary for La Liga")
    print("=" * 40)
    for match in data["events"]:
            print(f"Date: {match['date'][:match['date'].find('T')]}")
            print(f"Teams: {match['competitions'][0]['competitors'][0]['team']['name']} vs {match['competitions'][0]['competitors'][1]['team']['name']}")
            print(f"Team 1 Logo: {match['competitions'][0]['competitors'][0]['team']['logo']}")
            print(f"Team 2 Logo:  {match['competitions'][0]['competitors'][1]['team']['logo']}")
            print(f"Score: {match['competitions'][0]['competitors'][0]['score']} - {match['competitions'][0]['competitors'][1]['score']}")
            print(f"Status: {match['competitions'][0]['status']['type']['description']}")
            soccer.append([match['competitions'][0]['competitors'][0]['team']['shortDisplayName'], match['competitions'][0]['competitors'][1]['team']['shortDisplayName'], match['competitions'][0]['competitors'][0]['team']['logo'], match['competitions'][0]['competitors'][1]['team']['logo'], match['competitions'][0]['competitors'][0]['score'], match['competitions'][0]['competitors'][1]['score'], match['competitions'][0]['status']['type']['description']])
            scorers = []
        
            # Loop through details to find goals
            for detail in match['competitions'][0]['details']:
                if detail['type']['id'] == "70":  # Check if it's a goal
                    for athlete in detail['athletesInvolved']:
                        scorers.append(f"{athlete['displayName']} ({detail['clock']['displayValue']})")
            
            # Print scorers if any
            if scorers:
                print("Scorers:")
                for scorer in scorers:
                    print(f"  - {scorer}")
            else:
                print("Scorers: None")
            
            print("-" * 40)
    print("=" * 40)


    #UCL
    data = requests.post("https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard")
    data = data.json()
    print("\nMatch Summary for Champions League")
    print("=" * 40)
    for match in data["events"]:
            print(f"Date: {match['date'][:match['date'].find('T')]}")
            print(f"Teams: {match['competitions'][0]['competitors'][0]['team']['name']} vs {match['competitions'][0]['competitors'][1]['team']['name']}")
            print(f"Team 1 Logo: {match['competitions'][0]['competitors'][0]['team']['logo']}")
            print(f"Team 2 Logo:  {match['competitions'][0]['competitors'][1]['team']['logo']}")
            print(f"Score: {match['competitions'][0]['competitors'][0]['score']} - {match['competitions'][0]['competitors'][1]['score']}")
            print(f"Status: {match['competitions'][0]['status']['type']['description']}")
            soccer.append([match['competitions'][0]['competitors'][0]['team']['shortDisplayName'], match['competitions'][0]['competitors'][1]['team']['shortDisplayName'], match['competitions'][0]['competitors'][0]['team']['logo'], match['competitions'][0]['competitors'][1]['team']['logo'], match['competitions'][0]['competitors'][0]['score'], match['competitions'][0]['competitors'][1]['score'], match['competitions'][0]['status']['type']['description']])
            scorers = []
        
            # Loop through details to find goals
            for detail in match['competitions'][0]['details']:
                if detail['type']['id'] == "70":  # Check if it's a goal
                    for athlete in detail['athletesInvolved']:
                        scorers.append(f"{athlete['displayName']} ({detail['clock']['displayValue']})")
            
            # Print scorers if any
            if scorers:
                print("Scorers:")
                for scorer in scorers:
                    print(f"  - {scorer}")
            else:
                print("Scorers: None")
            
            print("-" * 40)
    print("=" * 40)


    #NBA
    game = requests.post("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard")
    game = game.json()
    print("\nMatch Summary for NBA")
    for match in game["events"]:
            print(f"Date: {match['date'][:match['date'].find('T')]}")
            print(f"Teams: {match['competitions'][0]['competitors'][0]['team']['name']} vs {match['competitions'][0]['competitors'][1]['team']['name']}")
            print(f"Team 1 Logo: {match['competitions'][0]['competitors'][0]['team']['logo']}")
            print(f"Team 2 Logo:  {match['competitions'][0]['competitors'][1]['team']['logo']}")
            print(f"Score: {match['competitions'][0]['competitors'][0]['score']} - {match['competitions'][0]['competitors'][1]['score']}")
            print(f"Status: {match['competitions'][0]['status']['type']['description']}")
            bball.append([match['competitions'][0]['competitors'][0]['team']['name'], match['competitions'][0]['competitors'][1]['team']['name'], match['competitions'][0]['competitors'][0]['team']['logo'], match['competitions'][0]['competitors'][1]['team']['logo'], match['competitions'][0]['competitors'][0]['score'], match['competitions'][0]['competitors'][1]['score'], match['competitions'][0]['status']['type']['description']])
            top_scorers = []
        
            # Loop through competitors to find top scorers
            for competitor in match['competitions'][0]['competitors']:
                for leader in competitor['leaders']:
                    if leader['name'] == 'points':
                        for scorer in leader['leaders']:
                            top_scorers.append(f"{scorer['athlete']['displayName']} ({scorer['displayValue']})")
            
            # Print top scorers if any
            if top_scorers:
                print("Top Scorers:")
                for scorer in top_scorers:
                    print(f"  - {scorer}")
            else:
                print("Top Scorers: None")

            print("-" * 40)
    print("=" * 40)


    #March Madness
    game = requests.post("https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard")
    game = game.json()
    print("\nMatch Summary for March Madness")
    for match in game["events"]:
            print(f"Date: {match['date'][:match['date'].find('T')]}")
            print(f"Teams: {match['competitions'][0]['competitors'][0]['team']['name']} vs {match['competitions'][0]['competitors'][1]['team']['name']}")
            print(f"Team 1 Logo: {match['competitions'][0]['competitors'][0]['team']['logo']}")
            print(f"Team 2 Logo:  {match['competitions'][0]['competitors'][1]['team']['logo']}")
            print(f"Score: {match['competitions'][0]['competitors'][0]['score']} - {match['competitions'][0]['competitors'][1]['score']}")
            print(f"Status: {match['competitions'][0]['status']['type']['description']}")
            madness.append([match['competitions'][0]['competitors'][0]['team']['name'], match['competitions'][0]['competitors'][1]['team']['name'], match['competitions'][0]['competitors'][0]['team']['logo'], match['competitions'][0]['competitors'][1]['team']['logo'], match['competitions'][0]['competitors'][0]['score'], match['competitions'][0]['competitors'][1]['score'], match['competitions'][0]['status']['type']['description']])
            top_scorers = []
        
            # Loop through competitors to find top scorers
            for competitor in match['competitions'][0]['competitors']:
                for leader in competitor['leaders']:
                    if leader['name'] == 'points':
                        for scorer in leader['leaders']:
                            top_scorers.append(f"{scorer['athlete']['displayName']} ({scorer['displayValue']})")
            
            # Print top scorers if any
            if top_scorers:
                print("Top Scorers:")
                for scorer in top_scorers:
                    print(f"  - {scorer}")
            else:
                print("Top Scorers: None")

            print("-" * 40)
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

    return soccer, bball, madness