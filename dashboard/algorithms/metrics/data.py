"""Prepare data for Plotly Dash."""
import os
import numpy as np
import pandas as pd

path_file = os.path.join(os.path.dirname(__file__), '../../',  'data', 'file.csv')

"""Variable global para almacenar la ruta del archivo cargado"""
global uploaded_file_path
uploaded_file_path = ''

"""Create Pandas DataFrame from local CSV."""
def create_dataframe_M():
    global uploaded_file_path
    if uploaded_file_path: # solo si uploaded_file_path esta llena
        os.replace(uploaded_file_path, path_file)
    df = pd.read_csv(path_file, header=None) ##Considerar si lleva o no encabezado
    return df, path_file