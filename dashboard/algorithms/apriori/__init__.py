import dash
from dash import dcc
from dash import html
import pandas as pd

from .data import create_dataframe_A
from .. import tools as tl
from . import method as met
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

    upload_component = tl.box_upload(path_file,dash_app)

    dash_app.layout = html.Div(children=[
        upload_component,
        html.Div(id='table-container')
    ])

    @dash_app.callback(Output('table-container', 'children'),
              [Input('upload-data', 'contents')])
    def update_output(contents):
        if contents is not None:
            _, content_string = contents.split(',')
            decoded = tl.base64.b64decode(content_string)
            with open(path_file, 'w') as f:
                f.write(decoded.decode("utf-8"))
            uploaded_file_path = path_file
            df = pd.read_csv(uploaded_file_path)
            render = render_results(df)
            return render
        else:
            return html.Div()


    return dash_app.server

## Sección de renderizado de los componentes al cargar CSV
def render_results(df):
    # Create Data Table
    table = tl.create_data_table(df)
    figure, res_df = met.method(df)

    # Convertir el DataFrame en una lista de diccionarios
    res_data = res_df.to_dict('records')

    # Create Layout
    layout = html.Div(
        children=[
            table,
            dcc.Graph(id="graph-distribution", figure=figure),
            html.Table(
                [html.Tr([html.Th(col) for col in res_df.columns])] +
                [html.Tr([html.Td(data[col]) for col in res_df.columns]) for data in res_data]
            )
        ],
        className='render-container',
        style={
            'width': '100%',
        }
    )
    return layout

### Ends shared section. Start individual section: