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
        #loads the csv file
        df = pd.read_csv(csv_file)

        #define the features
        categorical_features = ['PROPERTY TYPE', 'CITY', 'ZIP OR POSTAL CODE']
        numeric_features = ['PRICE', 'LATITUDE', 'LONGITUDE']

        #select relevant columns for modeling
        selected_columns = ['BEDS'] + categorical_features + numeric_features
        #sets the columns to the columns in the dataframe
        df_selected = df[selected_columns]

        #separate data into features (X) and target variable (y)
        X = df_selected.drop('BEDS', axis=1)
        y = df_selected['BEDS']

        #handle missing values in the target variable 'y'
        imputer = SimpleImputer(strategy='mean')
        #creates imputer object to fill missing values
        y_imputed = imputer.fit_transform(y.values.reshape(-1, 1))
        #creates flattened version of y_imputed array
        y = pd.Series(y_imputed.flatten(), name='BEDS')

        #handle categorical features using one-hot encoding
        X_encoded = pd.get_dummies(X, columns=categorical_features)

        #split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, 
                                                            test_size=0.2, 
                                                            random_state=42)

        #train a Linear Regression model
        model = LinearRegression()
        #fits the model with the train data
        model.fit(X_train, y_train)

        #predict 'BEDS' values for rows with missing values
        X_missing_bed = X_encoded[df['BEDS'].isnull()]
        predicted_bed_values = model.predict(X_missing_bed)

        #update the 'BEDS' column with the predicted values
        df.loc[df['BEDS'].isnull(), 'BEDS'] = predicted_bed_values

        #saves it to the csv
        df.to_csv(csv_file, index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


#example usage:
csv_file_path = "feature_prediction.csv"
compute_null_bed(csv_file_path)


