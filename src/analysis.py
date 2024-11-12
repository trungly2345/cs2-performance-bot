
from demoparser2 import DemoParser
import pandas as pd
print("hello")
#initalize parser with with the file demo path
# Initialize parser with the demo file path
parser = DemoParser("nuke_oct_27.dem")

MY_STEAM_ID = 76561199403108558

# Parse all events

df = parser.parse_event("player_death", player=["last_place_name"])
df_coords = df[["attacker_posX", "attacker_posY", "user_posX", "user_posY"]]
print(df_coords.head())
if df.empty:
    print("No data")

else:
    print(df.head())

df["attacker_steamid"] = df["attacker_steamid"].astype(int)
df["user_steamid"] = df["user_steamid"].astype(int)



# Get kills and deaths from the df and add them to a new df
my_kills = df[df["attacker_steamid"] == MY_STEAM_ID]
my_deaths = df[df["user_steamid"] == MY_STEAM_ID]


print(f"My Kills:\n{my_kills}")
print(f"My Deaths:\n{my_deaths}")


# get a list of all zones
all_unique_zones = my_kills["attacker_last_place_name"].unique().tolist()
all_unique_zones.extend(my_deaths["user_last_place_name"].unique())

if not all_unique_zones:
    print("No data")
    exit()

else: 
        # iterate through the zones and get the kills and deaths for each zone
    for zone in all_unique_zones:
        num_kills = len(my_kills[my_kills["attacker_last_place_name"] == zone])
        num_deaths = len(my_deaths[my_deaths["user_last_place_name"] == zone])

        # print the results
        print(f"Zone: {zone}")
        print(f"Kills: {num_kills}")
        print(f"Deaths: {num_deaths}")
        print("\n")



