import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

summary_df = pd.read_excel("summary_gesamt1_5.xlsx")
del summary_df["Unnamed: 0"]

# DataFrame erstellen

summary_df['Monat/Jahr'] = pd.to_datetime(summary_df['Monat/Jahr'], format='%b %Y')

# Dash App erstellen
app = dash.Dash(__name__)

# Layout der App definieren
app.layout = html.Div([
    html.H1("Unternehmensgeschäftsbericht"),

    dcc.Slider(
        id='year-slider',
        min=summary_df['Monat/Jahr'].dt.year.min(),
        max=summary_df['Monat/Jahr'].dt.year.max(),
        value=summary_df['Monat/Jahr'].dt.year.max(),
        marks={year: year for year in summary_df['Monat/Jahr'].dt.year.unique()},
        step=1
    ),

    dcc.Graph(id='sales-overview'),
    dcc.Graph(id='product-performance'),
    dcc.Graph(id='profit-margin')
], style={'width': '80%', 'margin': 'auto'})



# Callback-Funktionen für die Aktualisierung der Diagramme basierend auf dem Slider
@app.callback(
    [Output('sales-overview', 'figure'),
     Output('product-performance', 'figure'),
     Output('profit-margin', 'figure')],
    [Input('year-slider', 'value')]
)
def update_figures(selected_year):
    filtered_df = summary_df[summary_df['Monat/Jahr'].dt.year == selected_year]

    # Sales Overview (Bar Chart)
    sales_fig = px.bar(
        filtered_df,
        x='Monat/Jahr',
        y='Produzierte Einheiten',
        title='Verkaufszahlen im Jahr {}'.format(selected_year),
        labels={'Produzierte Einheiten': 'Verkaufte Einheiten'}
    )

    # Product Performance (Bar Chart)
    product_perf_fig = px.bar(
        filtered_df,
        x='Monat/Jahr',
        y='Bruttogewinnspanne',
        color='Produkttyp Name',
        title='Bruttogewinnspanne pro Produkt im Jahr {}'.format(selected_year),
        labels={'Bruttogewinnspanne': 'Bruttogewinnspanne (%)'}
    )

    # Profit Margin (Bar Chart)
    profit_margin_fig = px.bar(
        filtered_df,
        x='Monat/Jahr',
        y='Bruttogewinnspanne',
        title='Bruttogewinnspanne Entwicklung im Jahr {}'.format(selected_year),
        labels={'Bruttogewinnspanne': 'Bruttogewinnspanne (%)'}
    )

    return sales_fig, product_perf_fig, profit_margin_fig


# App starten
if __name__ == '__main__':
    app.run_server(debug=True)
# %%
