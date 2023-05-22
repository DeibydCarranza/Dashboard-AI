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
            #render = render_results(df,dash_app)
            return render
        else:
            return html.Div()
    return dash_app.server

#Renderizado de los componentes al cargar un archivo
def render_results(df,section_params,dash_app):
#def render_results(df,dash_app):

    # Create Data Table y algoritmo funcional
    table = tl.create_data_table(df)
    figure = met.methodGraph(df)
    res_df = met.application(df,0.01,0.3,2.3)

    # Convertir el DataFrame en una lista de diccionarios
    res_data = res_df.to_dict('records')
    res_data = [data for data in res_data if isinstance(data, dict)]

    # Generar los títulos de la tabla y sus filas
    title_row = html.Tr([html.Th(col) for col in res_data[0].keys()] + [html.Th("Acciones")])
    titles = html.Thead(title_row)
    card_rows = []
    for index, data in enumerate(res_data):
        card_rows.extend(generate_card(data, index,res_data))

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
    section_mod1 = mod_params_slide_input(dash_app, 0, 1, "-1")
    section_mod2 = mod_params_slide_input(dash_app, 0, 2, "-2")
    section_mod3 = mod_params_slide_input(dash_app, 0, 6, "-3")

    # Variables para almacenar los valores de los componentes
    value_1 = (section_mod1.children[0].value, section_mod1.children[1].value)
    value_2 = (section_mod2.children[0].value, section_mod2.children[1].value)
    value_3 = (section_mod3.children[0].value, section_mod3.children[1].value)
    print(value_1)
    @dash_app.callback(
        Output("output-container", "children"),
        [Input("input-circular-1", "value"),
         Input("input-circular-2", "value"),
         Input("input-circular-3", "value"),
         Input("slider-circular-1", "value"),
         Input("slider-circular-2", "value"),
         Input("slider-circular-3", "value")]
    )
    def update_output(*values):
        return html.Div([
            f"Value 1: {values[0]}, Slider Value 1: {values[3]}",
            html.Br(),
            f"Value 2: {values[1]}, Slider Value 2: {values[4]}",
            html.Br(),
            f"Value 3: {values[2]}, Slider Value 3: {values[5]}"
        ])
        #return met.method(dash_app,values[0],values[1],values[2])

    layout = html.Div(
        children=[
            section_mod1,
            section_mod2,
            section_mod3,
            html.Div(id="output-container")  # Contenedor para mostrar los valores
        ],
        className='block-params-container'
    )
    return layout


# Componente dual Slider-Input. Los sufijos ayudan a no duplicarlos
def mod_params_slide_input(app, mini, maxi, suffix=""):
    input_id = "input-circular" + suffix
    slider_id = "slider-circular" + suffix

    section_mod = html.Div(
        children=[
            dcc.Slider(
                id=slider_id,
                min=mini,
                max=maxi,
                marks={i: str(i) for i in range(maxi + 1)},
                value=(maxi / 3)
            ),
            dcc.Input(
                id=input_id,
                type="number",
                min=mini,
                max=maxi,
                value=(maxi / 3)
            )
        ],
        className='slider-input-container'
    )

    @app.callback(
        [Output(input_id, "value"), Output(slider_id, "value")],
        [Input(input_id, "value"), Input(slider_id, "value")]
    )
    def update_output(input_value, slider_value):
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        value = input_value if trigger_id == input_id else slider_value
        return value, value

    return section_mod

# Generación de los componentes tipo tabla donde se muestran las reglas
def generate_card(data, index,res_data): 
    if not data:
        return None

    id_str = f"toggle-button-{index}"
    description = html.Div(
        html.P('Tomando como antecedente ' +str(res_data[index]['Antecedente']+' existe un aumento de posibilidades de  '
            +str(res_data[index]['Elevación'])+ ' veces para consumir igualmente '+str(res_data[index]['Consecuente'])+'. Tal que se tiene una confianza del '
            +str(res_data[index]['Confianza'])+' considerando una importancia de la regla del '+str(res_data[index]['Soporte'])),
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