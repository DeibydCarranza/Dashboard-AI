import dash
from dash import dash_table,dcc,html,Output,Input
import base64
import pandas as pd
import os

global path_file
path_file = os.path.join(os.path.dirname(__file__), '../',  'data', 'file.csv')


""" Generate update component (just html) """
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

""" Create and return dash_table """
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

""" Save data on file, generete dataframe and return dash_tabe """
def parse_contents(contents, filename):
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    global path_file
    try:
        if 'csv' in filename:
            print("------->" + filename)
            # writin on file
            write_on_file(decoded)
            print("---->")
            print(path_file)
            # generating dataframe
            df = pd.read_csv(path_file, header=None) ##Considerar si lleva o no encabezado
            print("-->")
            # Generate html component
            render = render_results(df)
            print("->")
    except Exception as e:
        print(e)
        return html.Div([
            'Archivo erroneo, solo archivos .csv'
        ])

    return render

""" Generate table """
def render_results(df):
    # Create Data Table
    table = create_data_table(df)

    # Create Layout
    res = html.Div(
        children=[
            table
        ],
        className='render-container',
        style={
            'width': '100%',
        }
    )
    return res

"""Create Pandas DataFrame from local CSV."""
def write_on_file(decoded):
    global path_file
    if not path_file: # solo si path_file no esta llena
        with open(path_file, 'w') as f:
                f.write(decoded.decode("utf-8"))

""" Componente dual Slider-Input. Los sufijos ayudan a no duplicarlos"""
def mod_params_slide_input(app, mini, maxi, suffix=""):
    section_mod = html.Div(children=(
            dcc.Slider(
                id="slider-circular" + suffix,
                min=mini,
                max=maxi,
                marks={i: str(i) for i in range(maxi + 1)},
                value=(maxi // 3)
            ),
            dcc.Input(
                id="input-circular" + suffix,
                type="number",
                min=mini,
                max=maxi,
                value=(maxi // 3)
            )
        ),
        className='slider-input-container'
    )

    @app.callback(
        [Output("input-circular" + suffix, "value"),
         Output("slider-circular" + suffix, "value")],
        [Input("input-circular" + suffix, "value"),
         Input("slider-circular" + suffix, "value")]
    )
    def update_output(input_value, slider_value):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        value = input_value if trigger_id == "input-circular" + suffix else slider_value
        return value, value

    return section_mod
