"""Instantiate a Dash app."""
import dash
from dash import dash_table
from dash import dcc
from dash import html
import pandas as pd

from .data import create_dataframe_A
from ..tools import *
from .layout import html_layout
from dash.dependencies import Input, Output, State

def init_dashboard_apriori(server):
    file_uploaded = False
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/apriori/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df, path_file = create_dataframe_A()

    # Custom HTML layout
    dash_app.index_string = html_layout

    upload_component = box_upload(path_file,dash_app)

    dash_app.layout = html.Div(children=[
        upload_component,
        render_results(dash_app,df)
    ])

    return dash_app.server


def create_data_table(df):
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=10,
        style_table={'overflowX': 'scroll','overflowY': 'scroll'}
    )
    return table

def render_results(dash_app,df):
    # Create Layout
    res = html.Div(
        children=[
            create_data_table(df)
        ],
        id="dash-container",
        style={
            'width': '100%',
        }
    )
    return res