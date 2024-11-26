# CS2 Performance Analysis Bot


## Preface
Faceit is a third party matchmaking system where you play competitive 5 vs 5 against people who are on the 
similar level as you with very strong Anti Cheat system. 
When I started playing FaceIt, I wanted to improve and have a goal in mind to get the the highest elo.
There are skill groups in FaceIt. Ranging from level 1 (lowest) to level 10 (highest).

My goal is to get Faceit Level 10. But I always started to ask myself how can I reach to level 10? 
I started breaking it down into smaller pieces. Like anything you want to become good at. I needed to start
with the fundlementals Counter Strike. And how can I track if I'm implementing the fundlementals correctly? 
This is how the project began. 



## Overview
This project is a **CS2 Faceit Performance Analysis Bot** designed to help me improve my competitive gameplay on Faceit by analyzing key metrics such as **positioning**, **K/D ratio**, and **impact kills**. The bot provides data-driven insights based on match history and demo file analysis.

## MVP Features

### 1. Data Collection
- **Goal**: Fetch match history and demo URLs from the Faceit API.
- **Tasks**:
  - Retrieve recent matches for a specific player. **completed**
  - Implement pagination to collect matches over a defined period (e.g., weekly). **completed**
  - Extract demo URLs for further analysis **completed**

### 2. Demo Parsing
- **Goal**: Extract in-game events from demo files.
- **Tasks**:
  - Parse demo files to capture:
    - **Kill Events**: Player kills, deaths, headshots. **completed**
    - **Positioning Data**: Player coordinates during key events. **in progress** 
    - **Round Outcomes**: Impact kills like clutches and entries. # need an idea how to implement this 

### 3. Key Performance Metrics Analysis
- **Goal**: Calculate essential performance metrics.
- **Tasks**:
  - **K/D Ratio**: Calculate kills-to-deaths ratio for each match. # complted 
  - **Impact Kills**: Identify impactful kills such as first kills, multi-kills, and clutches. # in progress 
  - **Map-Specific Performance**: Track performance on specific maps. # in progress 

### 4. Basic Positioning Insights
- **Goal**: Analyze player positioning and visualize risk zones.
- **Tasks**:
  - Generate basic **heatmaps** for kill and death positions.
  - Highlight high-risk areas where the player frequently dies.

### 5. Feedback Delivery
- **Goal**: Provide actionable performance insights.
- **Tasks**:
  - Summarize performance for each match, including:
    - K/D ratio
    - Impact kills
    - Positioning highlights
  - Deliver feedback via:
    - **Command-line output** (initial MVP).
    - *(Optional for future)* Integration with Discord or Telegram for delivering insights.

## Future Enhancements (Post-MVP)
- **Advanced Positioning Analysis**: Use clustering algorithms to detect patterns and suggest positioning improvements.
- **Goal Tracking**: Allow players to set and track specific performance goals.
- **Real-Time Insights**: Provide live feedback during matches if supported by API data.
- **Interactive UI**: Develop a web or mobile interface for improved user experience.

## Tech Stack
- **Python**: Core language for data collection, parsing, and analysis.
- **Flask**: (Optional) For server-side API requests and data processing.
- **Matplotlib / Plotly**: For generating heatmaps and visualizing positioning data.
- **SQLite**: Local database for storing match and player data.
- **Faceit API**: For retrieving match history and demo URLs.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cs2-performance-bot.git


  
