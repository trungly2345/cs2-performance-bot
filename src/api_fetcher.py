import requests

API_KEY = "99366875-fbd1-4080-8e8c-4c45829fe466"
player_id = "tommyy_24"
game = "CS2"

headers = {
    "authorization" : f"Bearer{API_KEY}"
}


# retrieve all matches from the past week
def get_all_matches():

    match_ids = []
    index  = 0
    limit = 100

    while True:
        url = f"https://open.faceit.com/data/v4/players/{player_id}/history?game={game}&index={index}&limit={limit}"


