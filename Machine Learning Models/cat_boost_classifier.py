import pandas as pd
from catboost import CatBoostClassifier

def cat_boost_predicton(csv_file):
    """Predicts the prices of house utilizing the catboosts CatBootClassifier 
    machine learning algorithm by splitting into test and train values and 
    getting the percent differnce in predicted and actual values.

    Args:
        csv_file(str): the file that contains the housing data set in csv file
            format.
    """