def add_beds(data):
    # Define the features (predictors) and the target variable
    categorical_features = ['SALE TYPE', 'PROPERTY TYPE', 'CITY', 'ZIP OR POSTAL CODE']
    numeric_features = ['PRICE', 'LATITUDE', 'LONGITUDE']

    # Perform one-hot encoding on the entire dataset
    data_encoded = pd.get_dummies(data, columns=categorical_features, drop_first=True)

    # Split the data into two subsets: one with missing 'BEDS' and one without
    data_missing = data_encoded[data_encoded['BEDS'].isnull()]
    data_not_missing = data_encoded[~data_encoded['BEDS'].isnull()]

    X = data_not_missing.drop(columns=['BEDS'])
    y = data_not_missing['BEDS']

    # Split the data with non-missing 'BEDS' into training and validation sets
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

    # Choose a predictive model (Random Forest Regressor in this example)
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the validation set
    y_pred = model.predict(X_valid)

    # Evaluate the model's performance
    mse = mean_squared_error(y_valid, y_pred)
    print(f"Mean Squared Error on Validation Set: {mse}")

    # Now, predict the missing 'BEDS' values in the subset with missing values
    X_missing = data_missing.drop(columns=['BEDS'])
    predicted_beds = model.predict(X_missing)

    # Impute the missing 'BEDS' values
    data_missing['BEDS'] = predicted_beds

    # Combine the subsets back into the original DataFrame
    data_combined = pd.concat([data_not_missing, data_missing], ignore_index=True)

    # If an output file is provided, save the data to the CSV file
    if output_file:
        data_combined.to_csv(output_file, index=False)

    return data_combined

# Example usage:
input_data = pd.read_csv('final_data_set.csv')
output_data = add_beds(input_data, 'add_beds.csv')
