import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor

#global variable to store the trained model
trained_model = None

def cat_boost_prediction(csv_file):
    """Trains the CatBoostRegressor model using the provided CSV file.

    Args:
        csv_file(csv): csv file that contains the data which is used to train 
            the model

    Returns:
        model: the CatBoost regressor with the train model fitted
    """
    
    #reads the csv_file and saves it in dataframe
    model_data = pd.read_csv(csv_file)
    #sets the features to the other columns that arent price
    features = model_data.drop(['PRICE'], axis=1)
    #sets the target to price
    target = model_data['PRICE']
    
    #split the dataset into training
    X_train, _, y_train, _ = train_test_split(features, target, 
                                              test_size=.000002, random_state=3)
    
    #sets the model the catboost regressor
    model = CatBoostRegressor()
    #fits the model to it
    model.fit(X_train, y_train)
    return model

def predict_price():
    """gets the values that are entered by the user and uses it to predict the
    price and returns information depending on if a price is entered.

    Yields:
        messageBox: shows the predicted price range if no price. Shows the
            predicted price and evalues deal if a price is given
    """
    try:
        #get user input from entry widgets
        feature1 = property_type_dropdown.get()  
        feature2 = city_dropdown.get()
        feature3 = float(entry_feature3.get())
        feature5 = float(entry_feature5.get()) if entry_feature5.get() else None        
        feature6 = float(entry_feature6.get())
        feature7 = float(entry_feature7.get())
        feature8 = float(entry_feature8.get())
        feature9 = float(entry_feature9.get())
        feature10 = float(entry_feature10.get())
        feature11 = float(entry_feature11.get())
        feature12 = float(entry_feature12.get())
        feature13 = float(entry_feature13.get())

        #assigns numeric value to differnt strings for the first 2 predictions.
        #This is because the features do not make sense to be numeric for the 
        #gui so it transforms it for them. 
        feature1 = {'Home': 1, 'Townhouse': 2}.get(feature1, 0)
        feature2 = {'Annapolis': 0, 'Eastport': 1, 'Baltimore': 2, 'Parkville': 3, 
            'Brooklyn': 4, 'Catonsville': 5, 'Baltimore City': 6, 
            'Mount Washington': 7, 'Curtis Bay': 8, 'Gwynn Oak': 9, 
            'Bethesda': 10, 'Chevy Chase': 11, 'Kensington': 12, 
            'Glen Echo': 13, 'Cabin John': 14, 'Bowie': 15, 'Mitchellville': 16,
            'Upper Marlboro': 17, 'Columbia': 18, 'Clarksville': 19, 
            'Elkridge': 20, 'Ellicott City': 21, 'Jessup': 22, 'Laurel': 23, 
            'Woodstock': 24, 'Marriottsville': 25, 'Frederick': 26, 
            'Gaithersburg': 27, 'North Potomac': 28, 'Montgomery Village': 29,
            'Damascus': 30, 'Darnestown': 31, 'Washington Grove': 32, 
            'Laytonsville': 33, 'Rockville': 34, 'Germantown': 35, 
            'Boyds': 36, 'Potomac': 37, 'North Bethesda': 38, 
            'Silver Spring': 39, 'Washington': 40, 'Takoma Park': 41, 
            'Wheaton': 42, 'Ashton': 43, 'Burtonsville': 44, 'Springdale': 45, 
            'Waldorf': 46, 'Accokeek': 47, 'White Plains': 48, 
            'Other': 49}.get(feature2, 0)

        #create a DataFrame with user input
        user_input = pd.DataFrame({
            'PROPERTY TYPE': [feature1],  
            'CITY': [feature2],
            'ZIP OR POSTAL CODE': [feature3],
            'PRICE': [feature5] if feature5 is not None else 0, 
            'BEDS': [feature6],
            'BATHS': [feature7],
            'SQUARE FEET': [feature8],
            'LOT SIZE': [feature9],
            '$/SQUARE FEET': [feature10],
            'LATITUDE': [feature11],
            'LONGITUDE': [feature12],
            'HOA/MONTH': [feature13],
        })

        # Ensure the model is trained 
        global trained_model
        #if the model isnt trained
        if trained_model is None:
            #sets the csv for the model
            csv_model = ("feature_prediction.csv")
            #trains the model with the cat_boost_prediction model with the
            #csv file
            trained_model = cat_boost_prediction(csv_model)
        
        #makes predictions on the user input
        predicted_price = trained_model.predict(user_input)[0]

        #if a price is provided
        if feature5 is not None:
            #evaluate the deal
            price_difference = predicted_price - feature5
            if price_difference <= -60000:
                deal_evaluation = 'Very Bad Deal'
            elif price_difference <= -40000:
                deal_evaluation = 'Bad Deal'
            elif price_difference <= -20000:
                deal_evaluation = 'Fair Deal'
            elif price_difference <= 30000:
                deal_evaluation = 'Good Price'
            else:
                deal_evaluation = 'Great Price'
        
            #rounds the price to the nearest thousand for readability
            rounded_price = round(predicted_price / 1000) * 1000
            #shows a message on the gui with the predicted price and 
            #evaulates the deal
            messagebox.showinfo('Prediction and Deal Evaluation',
                                f'Given Price: ${round(feature5)}\n' 
                                f'Predicted Price: ${rounded_price}\n'
                                f'Deal Evaluation: {deal_evaluation}')

        #if there is no price inserted
        else:
            # rounds the price to the nearest thousand for readability
            rounded_price = round(predicted_price / 1000) * 1000
            # shows a message on the gui with the predicted price range
            messagebox.showinfo('Predicted Price', 
                    f'Predicted Price: ${(rounded_price + 2000)} to '
                    f'${(rounded_price - 20000)}')

    #if there is an error throughs the message
    except ValueError:
        messagebox.showerror('Error', 
                             'Please enter valid numeric values for features.')

#create the gui window
app = tk.Tk()
#titles it 
app.title('House Price Prediction')

#creates a property type dropdown.
label_feature1 = tk.Label(app, text='Property Type (Home or Townhouse):')
label_feature1.grid(row=0, column=0, padx=10, pady=10)
property_type_var = tk.StringVar()
property_type_var.set('Home')
property_type_dropdown = ttk.Combobox(app, textvariable=property_type_var, 
                                      values=['Home', 'Townhouse'])
property_type_dropdown.grid(row=0, column=1, padx=10, pady=10)

#creates a city drop down for the cities
label_feature2 = tk.Label(app, text='City:')
label_feature2.grid(row=1, column=0, padx=10, pady=10)
city_var = tk.StringVar()
city_var.set('View Dropdown') 
city_dropdown = ttk.Combobox(app, 
                             textvariable=city_var,
                               values=['Annapolis',  'Eastport', 'Baltimore', 
                                       'Parkville', 'Brooklyn', 'Catonsville', 
                                       'Baltimore City', 'Mount Washington', 
                                       'Curtis Bay', 'Gwynn Oak', 'Bethesda', 
                                       'Chevy Chase', 'Kensington', 'Glen Echo', 
                                       'Cabin John', 'Bowie', 'Mitchellville', 
                                       'Upper Marlboro', 'Columbia', 
                                       'Clarksville', 'Elkridge', 
                                       'Ellicott City', 'Jessup', 'Laurel', 
                                       'Woodstock', 'Marriottsville', 
                                       'Frederick', 'Gaithersburg', 
                                       'North Potomac', 'Montgomery Village', 
                                       'Damascus', 'Darnestown', 
                                       'Washington Grove', 'Laytonsville', 
                                       'Rockville', 'Germantown', 'Boyds', 
                                       'Potomac', 'North Bethesda', 
                                       'Silver Spring', 'Washington', 
                                       'Takoma Park', 'Wheaton', 'Ashton', 
                                       'Burtonsville', 'Springdale', 'Waldorf', 
                                       'Accokeek', 'White Plains', 'Other'])
city_dropdown.grid(row=1, column=1, padx=10, pady=10)

#creates a fill in the blank box for different features
#saves the entry and positions the grid
label_feature3 = tk.Label(app, text='Zip Code:')
label_feature3.grid(row=2, column=0, padx=10, pady=10)
entry_feature3 = tk.Entry(app)
entry_feature3.grid(row=2, column=1, padx=10, pady=10)

label_feature5 = tk.Label(app, text='Price:')
label_feature5.grid(row=4, column=0, padx=10, pady=10)
entry_feature5 = tk.Entry(app)
entry_feature5.grid(row=4, column=1, padx=10, pady=10)

label_feature6 = tk.Label(app, text='Number of beds:')
label_feature6.grid(row=6, column=0, padx=10, pady=10)
entry_feature6 = tk.Entry(app)
entry_feature6.grid(row=6, column=1, padx=10, pady=10)

label_feature7 = tk.Label(app, text='Number of Baths:')
label_feature7.grid(row=7, column=0, padx=10, pady=10)
entry_feature7 = tk.Entry(app)
entry_feature7.grid(row=7, column=1, padx=10, pady=10)

label_feature8 = tk.Label(app, text='Square feet:')
label_feature8.grid(row=8, column=0, padx=10, pady=10)
entry_feature8 = tk.Entry(app)
entry_feature8.grid(row=8, column=1, padx=10, pady=10)

label_feature9 = tk.Label(app, text='Lot Size:')
label_feature9.grid(row=9, column=0, padx=10, pady=10)
entry_feature9 = tk.Entry(app)
entry_feature9.grid(row=9, column=1, padx=10, pady=10)

label_feature10 = tk.Label(app, text='Price Per a Square Foot:')
label_feature10.grid(row=10, column=0, padx=10, pady=10)
entry_feature10 = tk.Entry(app)
entry_feature10.grid(row=10, column=1, padx=10, pady=10)

label_feature11 = tk.Label(app, text='Latitude:')
label_feature11.grid(row=12, column=0, padx=10, pady=10)
entry_feature11 = tk.Entry(app)
entry_feature11.grid(row=12, column=1, padx=10, pady=10)

label_feature12 = tk.Label(app, text='Longitude:')
label_feature12.grid(row=13, column=0, padx=10, pady=10)
entry_feature12 = tk.Entry(app)
entry_feature12.grid(row=13, column=1, padx=10, pady=10)

label_feature13 = tk.Label(app, text='HOA Cost per a Month:')
label_feature13.grid(row=14, column=0, padx=10, pady=10)
entry_feature13 = tk.Entry(app)
entry_feature13.grid(row=14, column=1, padx=10, pady=10)

#creates button which predicts the price
catboost_button = tk.Button(app, text='House Price Prediction', 
                            command=predict_price)
catboost_button.grid(row=15, column=0, columnspan=2, pady=10)

#start the main event loop
app.mainloop()