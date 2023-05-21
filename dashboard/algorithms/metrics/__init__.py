import dash
from dash import dash_table,dcc,html,Input, Output, State
import pandas as pd
from . import layout
from . import data
from .. import tool as tl

#Create a Plotly Dash dashboard
def init_dashboard_metrics(server):
    dash_app = dash.Dash(
        server=server, # server is a flask instance
        routes_pathname_prefix="/metricas/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )
    # Custom HTML layout
    dash_app.index_string = layout.html_layout
    # Load DataFrame & path
    df, path_file = data.create_dataframe_M()
    upload_component = tl.box_upload()


    # define body of page
    dash_app.layout = html.Div(children=[
        upload_component
    ])

    def parse_contents(contents, filename):
        if ',' not in contents:
            return html.Div([
                'Contenido incorrecto'
            ])
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        global uploaded_file_path
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                with open(path_file, 'w') as f:
                    f.write(decoded.decode("utf-8"))
                uploaded_file_path = path_file
        except Exception as e:
            print(e)
            return html.Div([
                'Archivo erroneo, solo archivos .csv'
            ])

        return html.Div([
            dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        )
        ])
    @dash_app.callback(Output('output-data-upload', 'children'),
                Input('upload-data', 'contents'),
                State('upload-data', 'filename'))
    def update_output(list_of_contents, list_of_names):
        if list_of_contents is not None:
            children = [
                parse_contents(c, n) for c, n in
                zip(list_of_contents, list_of_names)]
            return children
    
    return dash_app.server