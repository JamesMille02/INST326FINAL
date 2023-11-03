import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def compute_null_bed(csv_file):
    """Creates values for the null bed values through machine learning.

    Args:
        csv_file(str): the file that is used for the overall machine learning 
            model which contains the bed column.
    
    Returns:
        The altered data set
    """
    pass

input_data = pd.read_csv('feature_prediction.csv')
output_data = compute_null_bed(input_data, 'feature_prediction')
