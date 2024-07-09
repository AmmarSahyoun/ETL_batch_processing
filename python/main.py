import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import mysql.connector
from sqlalchemy import create_engine


def etl(excel_file):
    df = pd.read_excel(excel_file)
    
    # Calculate two metrics
    max_dau_by_network = df.groupby(['Date', 'Network'])['Daily Active Users'].max().reset_index(name='max_dau')
    most_active_networks = (
        max_dau_by_network.sort_values(by='max_dau', ascending=False).groupby('Date').head(1).sort_values(by='Date', ascending=True)
            )
 
    conversion_rates = df.groupby(["Date", "Network"]).agg(conversion_rate=("Subscription started", lambda x: x.mean() / df["Installs"].mean())).reset_index()
    best_conversion_network = (
        conversion_rates.sort_values(by='conversion_rate', ascending=False).groupby('Date').head(1).sort_values(by='Date', ascending=True)
            )
    print('2 Metrics have been calculate!')
    return most_active_networks, best_conversion_network

def create_plots(most_active_networks, best_conversion_network):
    fig1 = px.line(most_active_networks, x='Date', y='max_dau', color='Network', markers=True, width=1200, height=600)
    fig2 = px.line(best_conversion_network, x='Date', y='conversion_rate', color='Network', markers=True, width=1200, height=600)
    print('Creating diagrams!')
    return fig1, fig2

def load_to_db(most_active_networks, best_conversion_network):
    engine = create_engine('mysql+mysqlconnector://root:rootpassword@mysql:3306/marketing_db')
    most_active_networks.to_sql('most_active_networks', engine, if_exists='replace', index=False)
    best_conversion_network.to_sql('best_conversion_network', engine, if_exists='replace', index=False)
    print('Metrics have been stored in the database!')    

def main():
    excel_file = 'appMarketing.xlsx'
    most_active_networks, best_conversion_network = etl(excel_file)

    load_to_db(most_active_networks, best_conversion_network)
    fig1, fig2 = create_plots(most_active_networks, best_conversion_network)

    print('Creating Dashboard')
    app = Dash(__name__)
    app.layout = html.Div(
        children=[
            html.H1(children='Mobile Applications Marketing Dashboard'),
            html.Div(children='User Engagement Metrics'),
            dcc.Graph(id='Network with most daily active user', figure=fig1),
            dcc.Graph(id='Network with best installs-subscription ratio',figure=fig2)
            ]
        )
    app.run_server(host="0.0.0.0", port=8050, debug=True, use_reloader=False)



if __name__ == "__main__":
    main()
