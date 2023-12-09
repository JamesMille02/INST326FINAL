import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def linear_regression_model(csv_file):
    """Predicts the prices of houses using scikit-learn's Linear Regression 
    machine learning algorithm by splitting into test and train values and 
    getting the mean absolute error (MAE) in predicted and actual values.

    Args:
        csv_file (str): The file that contains the housing dataset in CSV file
            format.

    Returns:
        float: The mean absolute error for comparing the model's accuracy.
    """
    #load the dataset into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    #specify features X
    features = df.drop('PRICE', axis=1)
    #sets the target of the machine learning to PRICE will be what the model
    #predicts 
    target = df['PRICE']

    #split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, 
                                                        test_size=0.1, 
                                                        random_state=1)

    #create and train the Linear Regression model
    model = LinearRegression()
    #splits the train data to the model
    model.fit(X_train, y_train)

    #make predictions on the test set
    y_pred = model.predict(X_test)

    #calculates the mean absolute error
    mean_absolute_error_value = mean_absolute_error(y_test, y_pred)

    return mean_absolute_error_value

#call and print the mean absolute error value
mean_absolute_error_value = linear_regression_model("feature_prediction.csv")
print(f"Mean Absolute Error: {mean_absolute_error_value}")

