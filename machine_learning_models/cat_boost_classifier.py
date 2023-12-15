import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def cat_boost_prediction(csv_file):
    """Predicts the prices of houses using the CatBoostRegressor machine learning 
    algorithm by splitting into test and train values and getting the difference 
    in predicted and actual values.

    Args:
        csv_file(str): the file that contains the housing dataset in CSV file
            format.

    Returns:
        A variable which contains the mean absolute error for comparing the 
        model's accuracy.
    """
    #load the dataset into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    #specify features X
    features = df.drop(['PRICE'], axis=1) 
    #sets the target of the machine learning to PRICE will be what the model
    #predicts 
    target = df['PRICE']

    #Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, 
                                                        test_size=0.000002, 
                                                        random_state=2)
    
    #create and train the CatBoostRegressor model
    model = CatBoostRegressor()
    #fits the train data to the model
    model.fit(X_train, y_train)
    #make predictions on the test set
    y_pred = model.predict(X_test)
    #calculates the mean absolute error
    mean_absolute_error_value = mean_absolute_error(y_test, y_pred)

    return mean_absolute_error_value

#call and print the mean absolute error value
mean_absolute_error_value = cat_boost_prediction("feature_prediction.csv")
print(f"Mean Absolute Error: {mean_absolute_error_value}")
