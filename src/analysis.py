import requests
from demoparser2 import DemoParser
import pandas as pd
import matplotlib.pyplot as plt


MY_STEAM_ID = 76561199403108558

parser = DemoParser("nuke_oct_27.dem")


df = parser.parse_event("player_death", player=["last_place_name",])



df["attacker_steamid"] = df["attacker_steamid"].astype(int)
df["user_steamid"] = df["user_steamid"].astype(int)



# Get kills and deaths from the df and add them to a new df
my_kills = df[df["attacker_steamid"] == MY_STEAM_ID]

my_deaths = df[df["user_steamid"] == MY_STEAM_ID]


kills_by_zone = my_kills.groupby('attacker_last_place_name').size()

death_by_zone = my_deaths.groupby('user_last_place_name').size() 

print("Raw Deaths Data:")
print(my_deaths[["user_last_place_name", "tick"]])

# Check for possible duplicate ticks
print("Unique Deaths by Tick:")
print(my_deaths.groupby("tick").size())

# Define valid gameplay range
start_tick = 1000  # Example start tick
end_tick = 105000  # Example end tick (set based on match data)

# Filter deaths within valid ticks
filtered_deaths = my_deaths[(my_deaths["tick"] >= start_tick) & (my_deaths["tick"] <= end_tick)]
print( "Filtered deaths" ,filtered_deaths)

all_zones = set(kills_by_zone.index).union(set(death_by_zone.index))


total_kills = 0
total_deaths = filtered_deaths.shape[0]

zone_data = []
    # iterate through the zones and get the kills and deaths for each zone
for zone in all_zones:
    num_kills = kills_by_zone.get(zone, 0)
    num_deaths = death_by_zone.get(zone, 0)

    total_kills += num_kills
    
    zone_data.append ({
        "Zone": zone,
        "Kills": num_kills,
        "Deaths": num_deaths
    })

    df = pd.DataFrame(zone_data)

    # print the results
    print(f"Zone: {zone}")
    print(f"Kills: {num_kills}")
    print(f"Deaths: {num_deaths}")
    print("\n")


    df.to_csv("zone_data.csv", index=False)

print(f"Total Kills: {total_kills}")
print(f"Total Deaths: {total_deaths}")
