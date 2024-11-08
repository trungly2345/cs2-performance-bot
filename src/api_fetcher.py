from binascii import Error
from datetime import datetime, timedelta

import requests
from flask import json
from requests import Response

API_KEY = "99366875-fbd1-4080-8e8c-4c45829fe466"
Playernickname= "tommyy_24"
GAME = "cs2"
Player_id =  "47a78e05-9312-4e28-9056-63cfdfbd8252"

headers = {
    "Authorization" : f"Bearer {API_KEY}",
    'Content-Type': 'application/json'
}



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
                "limit" : 50
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
                total_matches = len(items)
                total_kills = sum(int(item['stats'].get('Kills'), 0) for item in items)
                total_deaths = sum(int(item['stats'].get('Deaths'), 0) for item in items)
                total_wins = sum(1 for item in items if item['stats'].get("Result", "0") == "1")
                total_headshots = sum(int(item['stats'].get("Headshots", 0)) for item in items)
                total_headshot_percentage = sum(int(item['stats'].get("Headshots %", 0)) for item in items)
               
                
                avg_headshot_percentage = total_headshot_percentage / total_matches if total_matches > 0 else 0
                win_rate = (total_wins / total_matches) * 100 if total_matches > 0 else 0
                avg_kd = total_kills / total_deaths if total_deaths > 0 else 0

               

                print(f"Summary of Overall Performance ({total_matches} Matches):")
                print(f"  Total Kills: {total_kills}")
                print(f"  Total Deaths: {total_deaths}")
                print(f"  Overall K/D Ratio: {avg_kd:.2f} ")
                print(f"  Win Rate: {win_rate:.2f}%")
                print(f"  Average Headshot Percentage: {avg_headshot_percentage:.2f}%")

        except KeyError as e:
                print(f"Error: Missing expected key {str(e)} in match data.")
        except ZeroDivisionError:
                print("Error: Division by zero occurred. No deaths recorded.")


if __name__ == "__main__":
       
       
        Playernickname = "tommyy_24"
        player_id = get_player_id(Playernickname)
        if player_id:
                stats = get_statistics(player_id)
                summarize_performance(stats)
                

        

