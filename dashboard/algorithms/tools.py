import dash
from dash import dash_table
from dash import dcc
from dash import html
import base64
from dash.dependencies import Input, Output, State

# Define el componente de carga de archivos
def box_upload(path_file,app):
    component = html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Carga de archivo ',
                html.A('Select CSV File')
            ]),
            style={
                'margin'
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '2px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '50px 10px'
            },
            # Permitir cargar múltiples archivos
            multiple=False
        ),
        html.Div(id='output-data-upload'),
    ])
    @app.callback(Output('output-data-upload', 'children'),
                  [Input('upload-data', 'contents')])
    def update_output(contents):
        if contents is not None:
            global uploaded_file_path
            _, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            with open(path_file, 'w') as f:
                f.write(decoded.decode("utf-8"))
            uploaded_file_path = path_file
    return component

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
