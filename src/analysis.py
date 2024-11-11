
from demoparser2 import DemoParser
import pandas as pd
#initalize parser with with the file demo path
# Initialize parser with the demo file path
parser = DemoParser("nuke_oct_27.dem")

# Parse all events
events = parser.parse_events(["all"])

# Convert the parsed events to a DataFrame if they are in a list format
if isinstance(events, list):
    df = pd.DataFrame(events)
    print("Parsed Events Sample:")
    print(df.head())  # Display the first few rows of the parsed events
else:
    print("Unexpected format of parsed events.")




