This is a housing price predictor created by James, PJ and Edwin for our INST326 final at the University of Maryland. This project allows a user to insert values and the machine learning model will determine the cost of the house and determine the quality of the deal. This is accomplished by downloading information off of redfin and pre-processing this data. From here, determined the appropraite model to use and implented it for the user input.

**Run the main portion of the code:**

  The result of our code was a graphical user interface that accepts different feature values. From here, these feature vaules are tested against our machine learning model and then a price is 
  predicted. In order to run this part of the code a user must type, python UI.py, use python3 if on mac when in the folder for the project. This will bring up a GUI which will have two dropdowns 
  and multiple empty boxes with labels. A user must choose the values for all no matter what for the code to run, except for the price. The price value is optional. When all information is   
  submitted the user must click the house price prediction button. From here, the machine learning model starts and will train the model and then predict the price. When the predicted price is 
  determined, two things could happen depending on if a price is given. If they do, it will show the predicted price, the inputed price, and will rate the deal. 
  If a price is not entered, then the predicted price range is shown.

**How to run code in command line:**

  In order to run the code in the command line, you must open the folder in the command line and then type python(3), 3 if on an mac, and then the file name
  for example you open the UI folder through cd yourpath/INST326Final/UI then you use python UI.py to run the UI file 

**How to run the code and interpret:**

  To run the code you can type python, python3 if you have a mac, and then the file name to run an file.
  The data cleaning file out put is formatted in a readable manner.
  The ML models display the average difference between the actual price. So if the output is 10,000, for a house of 200,000 the model will give a number between 210,000 and 190,000.
  For the GUI, the GUI displays a message. The message will depend on if the user adds a price. If they do, it will show the predicted price, the inputed price, and will rate the deal. 
  If a price is not entered, then the predicted price range is shown.

  **Unit Tests:**
There are unit test in place for the beds_prediction and data cleaning file. There is no unit tests for the ML models or the gui because the model displays errors and if the format of anything is
not correct an error will be displayed. Also, displaying the mean absolute value or the price allows the user to determine the validaty of the test without going through a test. So, due to these
reasons we decided unit tests for the models was unnecessary.

  **How to run every file:**
  
**data_set_prep folder:**
  cd file_path_to\INST326FINAL\data_set_prep
    python data_cleaning.py
      There are methods that have logic for the code to run also tests to determine validaty.
    python beds_prediction.py
      Method throws an error because there are no null values; however, there is unit tests that displays the method works.

**housing_price_gui folder:**
  cd file_path_to\INST326FINAL\housing_price_gui
    python UI.py
      brings up the GUI after a few seconds

**machine_learning_models folder**
  cd file_path_to\INST326FINAL\machine_learning_models
    python cat_boost_classifier.py
    python linear_regression.py
    python random_forest.py
    python ridge_regression.py
    python svm.py

**unit_tests folder:**
  cd file_path_to\INST326Final
    python -m unit_tests.beds_prediction_testing
    python -m unit_tests.data_cleaning_tests 


**Sources:**
  **For ML:**
  
1.4. Support Vector Machines. scikit. (n.d.-a). https://scikit-learn.org/stable/modules/svm.html This is the documentation for the machine learning algorithm, support vector machine. This algorithm was used while testing the accuracy for different algorithms. This webpage allowed us to accurately implement the model and test the results accuracy of the model against the different models.

Catboostclassifier. CatBoost. (n.d.). https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier This webpage is the documentation for the catboostclassifier. This is a library that has a ML model that is used in the program. This webpage was necessary to gain an understanding of how the model works and the requirements for it to work.

GeeksforGeeks. (2023, April 30). House price prediction using machine learning in Python. GeeksforGeeks. https://www.geeksforgeeks.org/house-price-prediction-using-machine-learning-in-python/ This page was used to get an understanding of how machine learning models are used for housing predictions and to determine the machine learning models that are best for housing predictions.

Ihre, A., &amp;  Engstrom, I. (n.d.). Predicting House prices with machine learning methods - diva. https://www.diva-portal.org/smash/get/diva2:1354741/FULLTEXT01.pdf This webpage was used to get an understanding of the process it takes to create a model to predict housing prices. It allowed us to understand what is necessary for the code and how to determine which features are best.

Sklearn.ensemble.randomforestregressor. scikit. (n.d.-b). https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html This is the webpage for the random forest regressor documentation. It is a linear regression model which uses multiple decision trees for one result. The webpage allowed us to implement the model accurately for our code.

Sklearn.linear_model.linearregression. scikit. (n.d.-c). https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html This webpages is the documentation for linear regression. This webpage gave us an understanding of how to implement linear regression in our model to determine its accuracy.

Sklearn.linear_model.Ridge. scikit. (n.d.-d). https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html This is the documentation for the ridge regression model. This webpage gave us an understanding of the model and how to implement it for our model in order to obtain accurate results.

GeeksforGeeks. (2021, November 28). How to calculate mean absolute error in python?. GeeksforGeeks. https://www.geeksforgeeks.org/how-to-calculate-mean-absolute-error-in-python/ This webpage gave us an understanding of a way to determine the accuracy of our models. It helped make it clear how to implement and use mean absolute error. The function allowed us to easily compare the accuracy of different models to determine the best one.

Sklearn.model_selection.train_test_split. scikit. (n.d.). https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html This documentation was used because it outlined the test train split method so we could split our csv and train the models and determine their validity.

Understanding train test split. Built In. (n.d.). https://builtin.com/data-science/train-test-split This webpage gave us the logic behind test train split and gave us a deeper understanding. This resulted in a better implementation which allowed us to appropriately train and test the model.
      
  **For GUI:**
  
GeeksforGeeks. (2023, January 6). Create first GUI application using Python-Tkinter. GeeksforGeeks. https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/ Our group had little idea how to create a gui for the user to input feature data Our group decided to use Tkinter for building our GUI. This page gave us an understanding of how Tkinter works and how to create the gui and accept user input.

Graphical user interfaces with TK. Python documentation. (n.d.). https://docs.python.org/3/library/tk.html This webpage is the documentation for Tkinter and allowed us to understand what was allowed in Tkinter and how to use it properly for our gui.

  **For User Input on GUI:**

Fitzpatrick, M. (2023, September 13). Validate user input when creating apps with Tkinter and python. Python GUIs. https://www.pythonguis.com/tutorials/input-validation-tkinter/ This file outlined user inputs in Tkinter and allowed us to be able to allow and handle user data for our model. This was a necessary step because without it our project idea would not have worked.Testing prediction model with user input.

Stack Overflow. (1965, December 1). https://stackoverflow.com/questions/58712891/testing-prediction-model-with-user-input We were struggling having the model run on the user input and the code given in the stackoverflow page was necessary to get it to function. The code is in our file and allows it to run how we desired.

  **For Unit testing:**

7.5. stringio - read and write strings as files¶. 7.5. StringIO - Read and write strings as files - Python 2.7.18 documentation. (n.d.). https://docs.python.org/2/library/stringio.html This documentation worked alongside the context manager to get the outputs and save them as the strings. This was very useful in order to compare the outputs of files. We used it to gather a greater understanding of how the module works and how to use it.

Contextlib - utilities for with-statement contexts. Python documentation. (n.d.-a). https://docs.python.org/3/library/contextlib.html Some of the methods in the data cleaning file has printed statements. This documentation allowed us to compare the output from calling the method to what was expected. This was useful when testing these methods because it allowed us to determine the validity of those method.

CSV - csv file reading and writing. Python documentation. (n.d.-b). https://docs.python.org/3/library/csv.html This webpage gave me the understanding of how to interact with csv files through code which was necessary to add remove read to csv files. This was necessary when cleaning the data.

GeeksforGeeks. (2020, December 11). Python tempfile module. GeeksforGeeks. https://www.geeksforgeeks.org/python-tempfile-module/ One of the methods through an error because the output was formatted as a list and this allowed us to compare a map to a map. This webpage was integral in comparing outputs of one method and allowed us to have an understanding of how the tempfile module works.

OS - miscellaneous operating system interfaces. Python documentation. (n.d.-c). https://docs.python.org/3/library/os.html This page outlined how the OS module works in python which was necessary because we needed to go to other files to add, combine, or remove information.

Testing#. Testing - pandas 2.1.4 documentation. (n.d.). https://pandas.pydata.org/docs/reference/testing.html This is the webpage for the documentation for the pandas testing module. This allowed us to understand how to run the tests and is used in the data_cleaning_file to determine the validatity of the code.

Unittest - unit testing framework. Python documentation. (n.d.-d). https://docs.python.org/3/library/unittest.html This is the documentation for the module unittest. This is the module we used for our unit tests. It was necessary to understand how unittest works and how to be able to tests through it.

  **Other Modules:**
  
OS - miscellaneous operating system interfaces. Python documentation. (n.d.-c). https://docs.python.org/3/library/os.html There were methods that needed to interact with the operating system and this documentation showed us how to do it. The methods needed to combine csvs and it had to take stored csv files.


