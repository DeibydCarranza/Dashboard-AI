#from application import app
from flask import current_app as app
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import os

@app.route('/')
def index():    

    return render_template('index.jinja2')

@app.route('/apriori/')
def apriori():
    # with open(os.path.join(os.path.dirname(__file__), '../../../', 'algorithms', 'layout2.jinja2'), 'r') as file:
    #     layout_A = file.read()
    with open(os.path.join(os.path.dirname(__file__), '../../' 'apriori/', 'layout2.jinja2'), 'r') as file: 
        layout_A = file.read()  
    return render_template(layout_A)
    #return render_template('index.jinja2')

@app.route('/chart1')
def chart1():

    # Graph One
    df = px.data.medals_wide()
    fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph two
    df = px.data.iris()
    fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species',  title="Iris Dataset")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('index.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON)

