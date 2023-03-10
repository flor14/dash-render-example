import altair as alt
from dash import dash, dcc, html, Input, Output
from vega_datasets import data
import dash_bootstrap_components as dbc

# Read in global data
cars = data.cars()

# Setup app and layout/frontend
app = dash.Dash(__name__, 
                 external_stylesheets=[dbc.themes.MINTY])
server = app.server

app.layout = html.Div([
    html.H1('Dash App'),
    html.Iframe(
        id='scatter',
        style={'border-width': '0',
              'width': '100%', 
              'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='Horsepower',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cars.columns]),
            dcc.Dropdown(
        id='ycol-widget',
        value='Displacement',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cars.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value'))
def plot_altair(xcol, ycol):
    chart = alt.Chart(cars).mark_point().encode(
        x=xcol,
        y=ycol,
        tooltip='Horsepower').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
