# CS2 Performance Analysis Bot

## Overview
This project is a **CS2 Performance Analysis Bot** designed to help players improve their competitive gameplay on Faceit by analyzing key metrics such as **positioning**, **K/D ratio**, and **impact kills**. The bot provides data-driven insights based on match history and demo file analysis.

## MVP Features

### 1. Data Collection
- **Goal**: Fetch match history and demo URLs from the Faceit API.
- **Tasks**:
  - Retrieve recent matches for a specific player. # completed 
  - Implement pagination to collect matches over a defined period (e.g., weekly). # completed 
  - Extract demo URLs for further analysis. # completed 

### 2. Demo Parsing
- **Goal**: Extract in-game events from demo files.
- **Tasks**:
  - Parse demo files to capture:
    - **Kill Events**: Player kills, deaths, headshots.
    - **Positioning Data**: Player coordinates during key events.
    - **Round Outcomes**: Impact kills like clutches and entries.

### 3. Key Performance Metrics Analysis
- **Goal**: Calculate essential performance metrics.
- **Tasks**:
  - **K/D Ratio**: Calculate kills-to-deaths ratio for each match.
  - **Impact Kills**: Identify impactful kills such as first kills, multi-kills, and clutches.
  - **Map-Specific Performance**: Track performance on specific maps.

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


  
