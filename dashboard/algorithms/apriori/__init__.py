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

    upload_component = box_upload(path_file)

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

    # Combinar los dos diseños
    dash_app.layout = html.Div(children=[
        upload_component,
        create_data_table(df)
    ])
    """
    @dash_app.callback(
        Output(component_id='database-table', component_property='data'),
        Input(component_id='upload-data', component_property='contents'),
        State(component_id='upload-data', component_property='filename')
    )
    def update_table(contents, filename):
        if contents is not None:
            content_type, content_string = contents.split(',')
            file = base64.b64decode(content_string)
            file_name = path_file  # agregar el timestamp al nombre del archivo
            with open(file_name, 'wb') as f:
                f.write(file)

            df = pd.read_csv(file_name)

            # Retorna los datos actualizados para la tabla
            return df.to_dict("records")

        # Si no se cargó un archivo, retorna los datos originales
        return df.to_dict("records")

    """
    return dash_app.server

