from binascii import Error
from datetime import datetime, timedelta

import requests
from flask import json
from requests import Response

API_KEY = "99366875-fbd1-4080-8e8c-4c45829fe466"
player_id = "tommyy_24"
game = "CS2"

headers = {
    "authorization" : f"Bearer{API_KEY}"
}

def get_weekly_timestamps():
        start_of_week = datetime.today() - timedelta(datetime.now().weekday())
        # calculate the start of "from" to end of "to" of the week
        from_timestamp = int(start_of_week.timestamp() * 1000)

        

# retrieve all matches from the past week
# we can do this from using from variable and to variable
def get_all_matches():
        #create url endpoint for all matches
        #what would a url endpoint would look like?
        #refer to faceit api documentation
        url = "https://open.faceit.com/data/v4/players/{player_id}/history"
        response = requests.get(url, headers=headers);

        # create a logic if status code == 200
        # how do i get a status code from
        if response.status_code == 200:
                # get the array of matches
                matches = response.json().get('data',[]); # get the matches data from the url endpoint
                match_ids = [match["match_id"] for match in matches]
                return match_ids
        else:
                print(f"Error: {response.status_code}, {response.text}")

                return []









