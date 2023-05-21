import dash
from dash import dash_table,dcc,html,Input, Output, State
import base64

# Define el componente de carga de archivos
def box_upload():
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