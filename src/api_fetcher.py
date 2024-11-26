from binascii import Error
from datetime import datetime, timedelta
import pandas as pd
import json

import requests
from flask import json
from requests import Response

API_KEY = "99366875-fbd1-4080-8e8c-4c45829fe466"
GAME = "cs2"
matchid = "1-a6bf2bdb-e532-4b52-9744-c7665bfa3713 "


headers = {
    "Authorization" : f"Bearer {API_KEY}",
    'Content-Type': 'application/json'
}

class DemoFetcher:
    def __init__(self, API_KEY):
        self.api_key = API_KEY

    def get_demo_url(self, match_id):
        # Example method to get demo URL
        # This is just a placeholder implementation
        match_details = get_match_details(match_id)
        if match_details:
                demourl = match_details.get('demo_url', ['N/A'])[0]
                print(f"Demo URL: {demourl}")
                return demourl
        else:
                print("Error: No match details found.")
                return None

    def download_demo_file(self, url, save_path):
        response = requests.get(url,stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded demo file to {save_path}")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None


def get_match_details(matchid):
      url = f"https://open.faceit.com/data/v4/matches/{matchid}"

      response = requests.get(url, headers=headers)

      if response.status_code == 200:
                match_details = response.json()
                return match_details
      else:
                print(f"Error: {response.status_code}, {response.text}")
                return None


def get_API_KEY():
    return API_KEY


def get_match_id():
      return matchid

def get_player_id(Playernickname):
        url = f"https://open.faceit.com/data/v4/players?nickname={Playernickname}"

        Response = requests.get(url, headers=headers)

        if Response.status_code == 200:
                player_id = Response.json().get('player_id')
                return player_id
        else:
                print(f"Error: {Response.status_code}, {Response.text}")
                return None

# retrieve all matches from the past week
# we can do this from using from variable and to variable
def get_all_matches(player_id):
        #create url endpoint for all matches
        #what would a url endpoint would look like?
        #refer to faceit api documentation
       
        url = f"https://open.faceit.com/data/v4/players/{player_id}/history"
        params = {
                "game" : GAME,
                "offset" : 0,
                "limit" : 50,
        }
        print("Request URL""", url)
        print("Request Params", params)
        response = requests.get(url, headers=headers,params=params)
        print("Response status code", response.status_code)
        print("Response text", response.text)

        # create a logic if status code == 200
        # how do i get a status code from
        if response.status_code == 200:
                # get the array of matches
                data = response.json().get('items',[])# get the matches data from the url endpoint
                return data
        else:
                print(f"Error: {response.status_code}, {response.text}")
                return []

def get_statistics(player_id):
        url = f"https://open.faceit.com/data/v4/players/{player_id}/games/{GAME}/stats"
        params = {
                "limit" : 50,
        }
        response = requests.get(url, headers=headers, params=params)

       
        if response.status_code == 200:
                data = response.json()
                return data

        else:
                print(f"Error: {response.status_code}, {response.text}")
                return None


def summarize_performance(statistics):
    if not statistics:
        print("Error: No stats found.")
        return 
    

    try:
        items = statistics['items']
        matches_data = []

        for item in items:
            match_id = item['stats'].get('Match Id', 'N/A')
            map = item['stats'].get('Map', 'N/A')
            kills = int(item['stats'].get('Kills', 0))
            deaths = int(item['stats'].get('Deaths', 0))
            kd_ratio = kills / deaths if deaths > 0 else 0
            headshots = int(item['stats'].get('Headshots', 0))
            headshot_percentage = int(item['stats'].get('Headshots %', 0))
            result = item['stats'].get("Result", "0")

        

             

            matches_data.append({
                "match_id" : match_id,
                "map" : map,
                "Kills" : kills,
                "Deaths" : deaths,
                "K/D Ratio" :kd_ratio,
                "headshots" : headshots,
                "headshot %" : headshot_percentage,
                "Result" : result,

                })


        
        df = pd.DataFrame(matches_data)
        
         # Summary calculations
        total_kills = df['Kills'].sum()
        total_deaths = df['Deaths'].sum()
        overall_kd_ratio = df['K/D Ratio'].mean()
        win_rate = (df['Result'] == "1").sum() / len(df) * 100
        avg_headshot_percentage = df['headshot %'].mean()
        map = df['map'].value_counts().idxmax()

      
       


         # Print summary
        print(f"\n{'Summary of Overall Performance':^50}")
        print(f"{'-'*50}")
        print(f"{'Total Matches':<25}: {len(df):>8}")
        print(f"{'Total Kills':<25}: {total_kills:>8}")
        print(f"{'Total Deaths':<25}: {total_deaths:>8}")
        print(f"{'Overall K/D Ratio':<25}: {overall_kd_ratio:>8.2f}")
        print(f"{'Win Rate':<25}: {win_rate:>8.2f}%")
        print(f"{'Average Headshot %':<25}: {avg_headshot_percentage:>8.2f}%")
        print(f"{'-'*50}\n")

        # Print detailed match summary
        print(f"{'Detailed Match Summary from the Past 50 matches':^50}")
        print(f"{'-'*50}")
        print(df.to_string(index=False))

       

        df.to_csv("matches.csv", index=False)
        print("Match data saved to matches.csv")

      



    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def summarize_match(match_details):
    if not match_details:
        print("Error: No match details found.")
        return

    try:
        # Pretty-print the JSON data
        print("Match Details received:")
        print(json.dumps(match_details, indent=4))

        
        teams = match_details.get('teams', {})
        map_name = match_details.get('voting', {}).get('map', {}).get('pick', ['N/A'])[0]
        demo_url = match_details.get('demo_url', ['N/A'])[0]
        match_id = match_details.get('match_id', 'N/A')
        region = match_details.get('region', 'N/A')
        results = match_details.get('results', {})

        matches_data = []

        for faction, details in teams.items():
            for player in details.get('roster', []):
                matches_data.append({
                    "faction": faction,
                    "game_player_name": player.get('game_player_name', 'N/A'),
                    "game_skill_level": player.get('game_skill_level', 'N/A'),
                    "map": map_name,
                    "demo_url": demo_url,
                    "match_id": match_id,
                    "results": results,
                    "region": region,
                })

        df = pd.DataFrame(matches_data)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', 50)
        pd.set_option('display.width', 1000)

        print("\nMatch Details in Tabular Format:")
        print(df[['faction', 'game_player_name', 'game_skill_level', 'map', 'region',]])

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("\n")
    Playernickname = "pienix"  # Replace with actual player nickname
    print("Fetching player ID...  " + Playernickname)
    player_id = get_player_id(Playernickname)
    print("Player ID", player_id)
    if player_id:
        stats = get_statistics(player_id)
        summarize_performance(stats)
        match_details = get_match_details(matchid)
        print("Match details:")
        summarize_match(match_details)

