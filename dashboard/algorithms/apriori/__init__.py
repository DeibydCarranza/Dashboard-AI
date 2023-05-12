"""Instantiate a Dash app."""
import dash
from dash import dash_table
from dash import dcc
from dash import html

from .data import create_dataframe
from .layout import html_layout
from dash.dependencies import Input, Output, State


def init_dashboard_apriori(server):
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
    #df = create_dataframe()

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Define el componente de carga de archivos
    upload_component = html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Inserta un archivo ',
                html.A('Select CSV File')
            ]),
            style={
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '2px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Permitir cargar múltiples archivos
            multiple=False
        ),
        html.Div(id='output-data-upload'),
    ])

    # Define el gráfico de dispersión
    scatter = {
        'x': [1, 2, 3, 4],
        'y': [10, 15, 13, 17],
        'mode': 'markers',
        'type': 'scatter'
    }

    layout = {
        'title': 'Gráfico de Dispersión Simple',
        'xaxis': {'title': 'Eje X'},
        'yaxis': {'title': 'Eje Y'}
    }

    fig = {'data': [scatter], 'layout': layout}

    scatter_graph = dcc.Graph(
        id="histogram-graph",
        figure=fig,
    )

    # Combinar los dos diseños
    dash_app.layout = html.Div(children=[
        html.H1(children='Mi primera aplicación Dash'),
        upload_component,
        scatter_graph,
    ])
    return dash_app.server

""""
def create_data_table(df):

    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
"""
