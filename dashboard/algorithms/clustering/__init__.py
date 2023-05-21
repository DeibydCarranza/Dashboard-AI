import dash
from dash import dash_table,dcc,html,Input, Output, State
from . import layout
from .. import tool as tl
#Create a Plotly Dash dashboard
def init_dashboard_metrics(server):
    """ Falk instance """
    dash_app = dash.Dash(
        server=server, # server is a flask instance
        routes_pathname_prefix="/clustering/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )
    """ Plugins """
    dash_app.index_string = layout.html_layout
    upload_component = tl.box_upload()

    """ Body """
    dash_app.layout = html.Div(children=[
        upload_component # Just import html structure
    ])
    """ Callbacks """
    @dash_app.callback(Output('output-data-upload', 'children'),
                Input('upload-data', 'contents'),
                State('upload-data', 'filename'))
    def update_output(list_of_contents, list_of_names):
        if list_of_contents is not None:
            children = [
                tl.parse_contents(list_of_contents, list_of_names)]
            return children
    
    return dash_app.server