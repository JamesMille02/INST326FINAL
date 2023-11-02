import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import Ridge
from sklearn.metrics import mean_squared_error

def linear_regression_model(csv_file):
    """Predicts the prices of house utilizing the sklearns Ridge machines 
    machine learning algorithm by splitting into test and train values 
    and getting the percent differnce in predicted and actual values.

    Args:
        csv_file(str): the file that contains the housing data set in csv file
            format.
    """