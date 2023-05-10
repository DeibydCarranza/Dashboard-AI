"""Prepare data for Plotly Dash."""
import os
import numpy as np
import pandas as pd

path_file = os.path.join(os.path.dirname(__file__), '../',  'data', 'file.csv')

def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv(path_file, parse_dates=["created"])

    """Data processing"""
    df["created"] = df["created"].dt.date
    df.drop(columns=["incident_zip"], inplace=True)
    num_complaints = df["complaint_type"].value_counts()
    to_remove = num_complaints[num_complaints <= 30].index
    df.replace(to_remove, np.nan, inplace=True)
    return df
