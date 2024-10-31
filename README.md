# NBA Team Visualization

This project is a Dash app that visualizes NBA team statistics from 2000 to 2023. The visualization uses team logos and custom styling to create an engaging, interactive interface. This guide will help you set up and run the project locally.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Project Structure

```plaintext
project_folder/
├── app.py                     # Main script to run the Dash app
├── nba_team_stats_00_to_23.csv # CSV file containing NBA team statistics data
├── requirements.txt           # List of dependencies
└── assets/
    ├── NBAlogos/              # Folder containing team logos used in the visualization
    └── styles.css             # Custom CSS for styling the visualization
```

## Setup Instructions
### *NOTE*: Step 1 not applicable if you already have the files (e.g. for InfoViz TA grading)
1. Clone the repository to your local machine.
```bash
git clone <https://github.com/ebb351/InfoVizHW3/tree/main>
cd project_folder
```
2. Set up a virtual environment.
```bash
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```
3. Install the required Python packages.
```bash
pip install -r requirements.txt
```

## Running the App
1. Run the Dash app.
```bash
python app.py
```
2. Open a web browser and navigate to `http://127.0.0.1:8050/` to view the app.

## Notes
- Make sure the `nba_team_stats_00_to_23.csv` file, `assets` folder with `NBAlogos`, and `styles.css` are in their respective locations as shown above.
- If you add any new dependencies, update the `requirements.txt` file using the following command:
```bash
pip freeze > requirements.txt
```