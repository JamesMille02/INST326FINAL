import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

def compute_null_bed(csv_file):
    """Creates values for the null bed values through machine learning.

    Args:
        csv_file (str): the file that is used for the overall machine learning 
            model which contains the 'bed' column.
    
    Returns:
        The altered dataset with imputed 'bed' values.
    """
    try:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file)

        # Define the features (predictors) and the target variable
        categorical_features = ['PROPERTY TYPE', 'CITY', 'ZIP OR POSTAL CODE']
        numeric_features = ['PRICE', 'LATITUDE', 'LONGITUDE']

        # Select relevant columns for modeling
        selected_columns = ['BEDS'] + categorical_features + numeric_features
        df_selected = df[selected_columns]

        # Separate data into features (X) and target variable (y)
        X = df_selected.drop('BEDS', axis=1)
        y = df_selected['BEDS']

        # Handle missing values in the target variable 'y'
        imputer = SimpleImputer(strategy='mean')
        y_imputed = imputer.fit_transform(y.values.reshape(-1, 1))
        y = pd.Series(y_imputed.flatten(), name='BEDS')

        # Handle categorical features using one-hot encoding
        X_encoded = pd.get_dummies(X, columns=categorical_features)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

        # Train a Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict 'bed' values for rows with missing values
        X_missing_bed = X_encoded[df['BEDS'].isnull()]
        predicted_bed_values = model.predict(X_missing_bed)

        # Update the 'bed' column with the predicted values
        df.loc[df['BEDS'].isnull(), 'BEDS'] = predicted_bed_values

        df.to_csv(csv_file, index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
csv_file_path = "feature_prediction.csv"
compute_null_bed(csv_file_path)


