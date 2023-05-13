import dash
from dash import dash_table
from dash import dcc
from dash import html
import pandas as pd

from .data import create_dataframe_M
from .. import tools as tl
from .layout import html_layout
from dash.dependencies import Input, Output, State

def init_dashboard_metrics(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/metricas/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df, path_file = create_dataframe_M()

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

### Ends shared section. Start individual section: