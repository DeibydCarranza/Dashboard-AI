"""Prepare data for Plotly Dash."""
import os
import numpy as np
import pandas as pd

path_file = os.path.join(os.path.dirname(__file__), '../../',  'data', 'file.csv')

def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv(path_file, parse_dates=["created"])

    """Data processing"""

    return df
