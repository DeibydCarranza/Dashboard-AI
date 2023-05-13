"""Prepare data for Plotly Dash."""
import os
import numpy as np
import pandas as pd
import re

path_file = os.path.join(os.path.dirname(__file__), '../../',  'data', 'temporal_Apriori.csv')

# Variable global para almacenar la ruta del archivo cargado
global uploaded_file_path
uploaded_file_path = ''

def create_dataframe_A():
    """Create Pandas DataFrame from local CSV."""
    global uploaded_file_path
    if uploaded_file_path:
        os.replace(uploaded_file_path, path_file)
    df = pd.read_csv(path_file, header=None)

    return df, path_file
