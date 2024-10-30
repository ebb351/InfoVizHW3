import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

#load data
df = pd.read_csv('nba_team_stats_00_to_23.csv')
df['year'] = df['season'].str.split('-').str[0]
df['year'] = df['year'].astype(int)
df.head()

team_logos = {
    'Boston Celtics': 'assets/NBALogos/celtics.png',
    'Denver Nuggets': 'assets/NBALogos/nuggets.png',
    'Oklahoma City Thunder': 'assets/NBALogos/thunder.png',
    'Minnesota Timberwolves': 'assets/NBALogos/timberwolves.png',
    'LA Clippers': 'assets/NBALogos/clippers.png',
    'Dallas Mavericks': 'assets/NBALogos/mavericks.png',
    'New York Knicks': 'assets/NBALogos/knicks.png',
    'Milwaukee Bucks': 'assets/NBALogos/bucks.png',
    'New Orleans Pelicans': 'assets/NBALogos/pelicans.png',
    'Phoenix Suns': 'assets/NBALogos/suns.png',
    'Cleveland Cavaliers': 'assets/NBALogos/caveliers.png',
    'Indiana Pacers': 'assets/NBALogos/pacers.png',
    'Los Angeles Lakers': 'assets/NBALogos/lakers.png',
    'Orlando Magic': 'assets/NBALogos/magic.png',
    'Philadelphia 76ers': 'assets/NBALogos/76ers.png',
    'Golden State Warriors': 'assets/NBALogos/warriors.png',
    'Miami Heat': 'assets/NBALogos/heat.png',
    'Sacramento Kings': 'assets/NBALogos/kings.png',
    'Houston Rockets': 'assets/NBALogos/rockets.png',
    'Chicago Bulls': 'assets/NBALogos/bulls.png',
    'Atlanta Hawks': 'assets/NBALogos/hawks.png',
    'Brooklyn Nets': 'assets/NBALogos/nets.png',
    'Utah Jazz': 'assets/NBALogos/jazz.png',
    'Memphis Grizzlies': 'assets/NBALogos/grizzlies.png',
    'Toronto Raptors': 'assets/NBALogos/raptors.png',
    'San Antonio Spurs': 'assets/NBALogos/spurs.png',
    'Charlotte Hornets': 'assets/NBALogos/hornets.png',
    'Portland Trail Blazers': 'assets/NBALogos/blazers.png',
    'Washington Wizards': 'assets/NBALogos/wizards.png',
    'Detroit Pistons': 'assets/NBALogos/pistons.png',
    'Los Angeles Clippers': 'assets/NBALogos/clippers.png',
    'Charlotte Bobcats': 'assets/NBALogos/bobcats.png',
    'New Orleans Hornets': 'assets/NBALogos/noHornets.png',
    'New Jersey Nets': 'assets/NBALogos/njNets.png',
    'Seattle SuperSonics': 'assets/NBALogos/sonics.png',
    'New Orleans/Oklahoma City Hornets': 'assets/NBALogos/okcHornets.png',
    'Vancouver Grizzlies': 'assets/NBALogos/vanGrizzlies.png'
}

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Label('Axis Scaling:'),
    dcc.RadioItems(
        id = 'axis-scaling',
        options = [
            {'label': 'Fit to Current View', 'value': 'fit'},
            {'label': 'Fixed Axes (useful for comparing across seasons)', 'value': 'fixed'}
        ],
        value = 'fit',
    ),

    dcc.Graph(id='scatter-plot'),

    html.Div([
        html.Div([
            html.Label('Select X-Axis'),
            dcc.RadioItems(
                id='x-axis',
                options=[
                    {'label': 'Points', 'value': 'points'},
                    {'label': 'Field Goal %', 'value': 'field_goal_percentage'},
                    {'label': '3P Attempts', 'value': 'three_pointers_attempted'},
                    {'label': '3P %', 'value': 'three_point_percentage'},
                    {'label': 'Rebounds', 'value': 'rebounds'},
                    {'label': 'Assists', 'value': 'assists'},
                    {'label': 'Turnovers', 'value': 'turnovers'},
                    {'label': 'Free Throw Attempts', 'value': 'free_throw_attempted'},
                ],
                value='points',  # default x-axis
            ),
        ], style={'flex': '1', 'margin-right': '10px'}),

        html.Div([
            html.Label('Select Year'),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].max(),
                step=1,
                marks={str(year): str(year) for year in df['year'].unique()},
            ),
        ], style={'flex': '4'}),
    ], style={'display': 'flex', 'alignItems': 'center'}),
])

# callback to update scatter plot based on x-axis and year selection
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('x-axis', 'value'),
     dash.dependencies.Input('year-slider', 'value'),
     dash.dependencies.Input('axis-scaling', 'value')]
)
def update_scatter_plot(x_axis, selected_year, axis_scaling):
    filtered_df = df[df['year'] == selected_year]

    x_axis_ranges = {
        'points': [5500, 10300],  # Example range for points
        'field_goal_percentage': [35, 55],  # Example range for FG%
        'three_pointers_attempted': [550, 3900],  # Example range for 3P attempts
        'three_point_percentage': [25, 45],  # Example range for 3P%
        'rebounds': [2500,4100],  # Example range for rebounds
        'assists': [1200, 2550],  # Example range for assists
        'turnovers': [700, 1550],  # Example range for turnovers
        'free_throw_attempted': [1100, 2600]  # Example range for plus/minus
    }

    x_axis_labels = {
        'points': 'Points',
        'field_goal_percentage': 'Field Goal %',
        'three_pointers_attempted': '3P Attempts',
        'three_point_percentage': '3P %',
        'rebounds': 'Rebounds',
        'assists': 'Assists',
        'turnovers': 'Turnovers',
        'free_throw_attempted': 'FT Attempts'
    }

    fig = px.scatter(filtered_df,
                     x = x_axis,
                     y = 'win_percentage',
                     hover_name = 'Team',
                     title = f'{selected_year} NBA Team Stats: {x_axis_labels[x_axis]} vs Win percentage',
                     labels = {'win_percentage': 'Win %', x_axis: x_axis_labels[x_axis]})

    if axis_scaling == 'fixed':
        x_range = x_axis_ranges.get(x_axis)
        fig.update_layout(
            xaxis=dict(range=x_axis_ranges.get(x_axis)),  #set x-axis range
            yaxis=dict(range=[0, 1])  #set y-axis range
        )
    else:
        x_range = [filtered_df[x_axis].min(), filtered_df[x_axis].max()]
        fig.update_layout(
            xaxis=dict(autorange = True),  #set x-axis range
            yaxis=dict(autorange = True)  #set y-axis range
        )

    # Calculate image size based on x-axis range
    x_range_diff = x_range[1] - x_range[0]
    if axis_scaling == 'fixed':
        image_size = 0.1 * (x_range_diff / 4)
    else:
        image_size = 0.1 * (x_range_diff / 3)  #adjust the divisor (larger divisor --> smaller image)

    # Add team logos as images
    for i, row in filtered_df.iterrows():
        fig.add_layout_image(
            dict(
                source=team_logos.get(row['Team']),
                x=row[x_axis],  # Position on the x-axis
                y=row['win_percentage'],  # Position on the y-axis
                xref="x",
                yref="y",
                sizex=image_size,  # Adjust the size as necessary
                sizey=image_size,
                xanchor="center",
                yanchor="middle"
            )
        )

    if selected_year == 2011:
        fig.add_annotation(
            text="Note: 2011 season had a lockout which led 66 games per team instead of 82",
            xref="paper", yref="paper",
            x=0.5, y=1.1, showarrow=False,
            font=dict(size=16, color="red"),
            align="center"
        )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)