import pandas as pd
from catboost import CatBoostClassifier

def cat_boost_predicton(csv_file):
    """Predicts the prices of house by splitting into test and train values
    and utilizing the catboosts CatBootClassifier 
    """