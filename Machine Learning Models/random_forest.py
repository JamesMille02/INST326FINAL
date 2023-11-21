import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

def random_forest_regression_model(csv_file):
    """Predicts the prices of houses using scikit-learn's Random Forest 
    regression machine learning algorithm by splitting into test and train values,
    handling infinity or large values, standardizing the data, and getting the 
    mean absolute error (MAE) in predicted and actual values.

    Args:
        csv_file (str): The file that contains the housing dataset in CSV file
            format.

    Returns:
        float: The mean absolute error for comparing the model's accuracy.
    """
    #load the dataset into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    #specifies features (X) and target variable (y)
    features = df.drop('PRICE', axis=1)
    target = df['PRICE']

    # Standardize the features
    scaler = StandardScaler()
    features_standardized = scaler.fit_transform(features)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features_standardized, 
                                                        target, test_size=0.2, 
                                                        random_state=42)

    #create and train the Random Forest Regressor model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    #fits the train data on the model
    model.fit(X_train, y_train)

    #makes predictions on the test set
    y_pred = model.predict(X_test)

    #calculates the mean absolute error
    mean_absolute_error_value = mean_absolute_error(y_test, y_pred)

    return mean_absolute_error_value

mean_absolute_error_value = random_forest_regression_model("feature_prediction.csv")
print(f"Mean Absolute Error: {mean_absolute_error_value}")
