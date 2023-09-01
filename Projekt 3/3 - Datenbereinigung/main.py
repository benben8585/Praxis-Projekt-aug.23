
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output




# Dash App erstellen
app = dash.Dash(__name__)


app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls'),  # Define the left element
                                  html.Div(className='eight columns div-for-charts bg-grey')  # Define the right element
                                  ])
                                ])


# App starten
if __name__ == '__main__':
    app.run_server(debug=True)
# %%