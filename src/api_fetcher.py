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
                "limit" : 20,
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
                data = response.json().get('items',[]); # get the matches data from the url endpoint
                return data
        else:
                print(f"Error: {response.status_code}, {response.text}")
                return []







if __name__ == "__main__":
       
       
        player_id = get_player_id(Playernickname)
        print("Player ID", player_id)
        matches = get_all_matches(player_id)
        print(matches)
        

