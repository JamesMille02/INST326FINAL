import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import mean_absolute_error

def cat_boost_predicton(csv_file):
    """Predicts the prices of house utilizing the catboosts CatBootClassifier 
    machine learning algorithm by splitting into test and train values and 
    getting the differnce in predicted and actual values.

    Args:
        csv_file(str): the file that contains the housing data set in csv file
            format.

    Returns:
        A variable which contains the mean absolute error for 
            comparing the models accuracy.
    """