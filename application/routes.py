#from application import app
from flask import current_app as app
from flask import render_template, request,redirect, url_for,Response
import pandas as pd
import json
import plotly
import plotly.express as px
import os
import csv
from sklearn.preprocessing import StandardScaler, MinMaxScaler 
from .Algorithms.Apriori.method import process_dataGraph,application
from scipy.spatial.distance import cdist 
import jsonify

global path_file,path_file_json
path_file = os.path.join(os.path.dirname(__file__), './data/', 'file.csv')
path_estandarizacion = os.path.join(os.path.dirname(__file__), './data/', 'escalamiento.csv')
path_file_json = os.path.join(os.path.dirname(__file__), '../', 'data.json')

@app.route('/')
def index():    
    return render_template('index.jinja2')

""" -------------- Algoritms ----------------"""

@app.route('/apriori/')
def apriori():
    df = pd.read_csv(path_file) 
    data = df.to_dict(orient='records')

    # Generar la gráfica y obtener el JSON
    graph_json = process_dataGraph(df)
    
    res_df = application(df,1,30,2.3)
    
    # Convertir el DataFrame en una lista de diccionarios
    res_data = res_df.to_dict('records')
    res_data = [data for data in res_data if isinstance(data, dict)]
    return render_template('layout_Apriori.jinja2', 
                title="Apriori", data=data, graph_json=graph_json, res_data=res_data)

@app.route('/clustering/')
def clustering():
    # Agregar la llamada a métodos de cada algoritmo
    return render_template('layout_Clustering.jinja2',
            title="Clustering")

@app.route('/metricas/')
def metricas():
    # Agregar la llamada a métodos de cada algoritmo
    return render_template('layout_Metricas.jinja2',
            title="Metricas")


""" -------------- Methods ----------------"""
# Decorador de carga para la carga y sobreescritura de los archivos
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    print("try...")
    if 'csv_file' not in request.files:
        return "No file uploaded"
    
    file = request.files['csv_file']

    if file.filename == '':
        return "No file selected"
    
    if file and file.filename.endswith('.csv'):
        csv_data = pd.read_csv(file)
        csv_data.to_csv(os.path.join(app.root_path, 'data/file.csv'), index=False)
        return "CSV file uploaded successfully and overwritten data.csv"
    else:
        return "Invalid file format. Please upload a CSV file."


@app.route('/standarizar')
def standarizar():
    print('Estandarizando')
    file = MinMaxScaler()
    MEstandarizada = file.fit_transform(pd.read_csv(path_file)) 
    DFrame_standar = pd.DataFrame(MEstandarizada) 
    DFrame_standar.to_csv(path_estandarizacion, index=False)
    return "Estandarizados"

@app.route('/normalizar')
def normalizar():
    print('Normalizando')
    file = StandardScaler()
    MEnormalizada = file.fit_transform(pd.read_csv(path_file)) 
    DFrame_standar = pd.DataFrame(MEnormalizada) 
    DFrame_standar.to_csv(path_estandarizacion, index=False)
    return "Normalizados"

@app.route('/read_csv')
def read_csv():
    df = pd.read_csv(path_estandarizacion)
    df_string = df.to_string(index=False)  # Convertir el DataFrame a una cadena
    return df_string

@app.route('/metricas')
def calcu_metrica():
    metrica = request.args.get('metrica')
    
    if metrica == 'chebyshev':
        pree_metrica = cdist(pd.read_csv(path_estandarizacion).values, pd.read_csv(path_estandarizacion).values, metric = metrica)
    elif metrica == 'euclidean':
        pree_metrica = cdist(pd.read_csv(path_estandarizacion).values, pd.read_csv(path_estandarizacion).values, metric = metrica)
    elif metrica == 'cityblock':
        pree_metrica = cdist(pd.read_csv(path_estandarizacion).values, pd.read_csv(path_estandarizacion).values, metric = metrica)
    elif metrica == 'minkowski':
        pree_metrica = cdist(pd.read_csv(path_estandarizacion).values, pd.read_csv(path_estandarizacion).values, metric = metrica, p=1.5)
    else:
        # Métrica no válida
        return jsonify({'error': 'Métrica no válida'})
    post_metrica = pd.DataFrame(pree_metrica)
    return post_metrica.to_json()
