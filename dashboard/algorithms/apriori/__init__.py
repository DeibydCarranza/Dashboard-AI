import dash
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output, State

from .data import create_dataframe_A
from .. import tools as tl
from . import method as met
from .layout import html_layout


def init_dashboard_apriori(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/apriori/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
        suppress_callback_exceptions=True
    )

    # Load DataFrame
    df, path_file = create_dataframe_A()

    # Custom HTML layout
    dash_app.index_string = html_layout

    upload_component = tl.box_upload(path_file, dash_app)
    dash_app.layout = html.Div(children=[
        upload_component,
        html.Div(id='table-container')
    ])

    #Renderizando el bloque Slider/Input
    section_params = block_params(dash_app)

    #Callback ejecutado para cargar un archivo
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
            render = render_results(df,section_params,dash_app)
            return render
        else:
            return html.Div()
    return dash_app.server

#Renderizado de los componentes al cargar un archivo
def render_results(df,section_params,dash_app):

    # Create Data Table y algoritmo funcional
    table = tl.create_data_table(df,)
    figure, res_df = met.method(df)

    # Convertir el DataFrame en una lista de diccionarios
    res_data = res_df.to_dict('records')
    res_data = [data for data in res_data if isinstance(data, dict)]

    # Generar los títulos de la tabla y sus filas
    title_row = html.Tr([html.Th(col) for col in res_data[0].keys()] + [html.Th("Acciones")])
    titles = html.Thead(title_row)
    card_rows = []
    for index, data in enumerate(res_data):
        card_rows.extend(generate_card(data, index))

    # Generar el cuerpo de la tabla con las filas de tarjetas
    card_body = html.Tbody(card_rows)
    table_rules = html.Table([titles, card_body], id="titulos")
    cards_container = html.Div(table_rules, className='cards-container')

    # Create Layout
    layout = html.Div(
        children=[
            table,
            dcc.Graph(id="graph-distribution", figure=figure),
            section_params,
            cards_container
        ],
        className='render-container',
        style={
            'width': '100%',
        }
    )
    return layout

# Bloque de slider/Input, se considera sufijos para identificarlos
def block_params(dash_app):
    section_mod1 = tl.mod_params_slide_input(dash_app, 0, 4, "-1")
    section_mod2 = tl.mod_params_slide_input(dash_app, 0, 10, "-2")
    section_mod3 = tl.mod_params_slide_input(dash_app, 0, 10, "-3")

    layout = html.Div(children=[
        section_mod1,
        section_mod2,
        section_mod3
    ],
    className='block-params-container'
    )
    return layout

# Generación de los componentes tipo tabla donde se muestran las reglas
def generate_card(data, index):
    if not data:
        return None

    id_str = f"toggle-button-{index}"
    description = html.Div(
        html.P('Holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ',
               id=f"descript-{index}",
               style={'display': 'none'},
               className="description_rule"),
    )
    button = html.Button(
        id=id_str,
        className='toggle-button',
        **{"data-target": index},
        children='Ver detalles',
        n_clicks=0,
        style={'margin-left': '10px'}
    )
    description_row = html.Tr([
        html.Td(
            html.Table(
                html.Tr(html.Td(description, colSpan='7')),
                className="nested-table"
            ),
            className="single-column-table",
            colSpan='7'
        )
    ], id=f"description-row-{index}")

    return [html.Tr([
                html.Td(str(value)) for value in data.values()
            ] + [html.Td(button)]),
            description_row]
