import dash
from dash import dash_table,dcc,html,Input, Output, State
from .. import layout
from .. import layouts  
from .. import callbacks
#Create a Plotly Dash dashboard
def init_dashboard_metrics(server):
    """ Falk instance """
    dash_app = dash.Dash(
        server=server, # server is a flask instance
        routes_pathname_prefix="/metricas/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )
    """ Plugins """
    dash_app.index_string = layout.html_layout

    """ Body """
    dash_app.layout = html.Div(children=[
        layouts.upLoad_component # Just import html structure
    ])    
    return dash_app.server