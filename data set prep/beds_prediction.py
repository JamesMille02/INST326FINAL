import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def compute_null_bed(data, output_file=None):
    pass

input_data = pd.read_csv('feature_prediction.csv')
output_data = compute_null_bed(input_data, 'feature_prediction')
