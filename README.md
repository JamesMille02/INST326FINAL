This is a housing price predictor created by James, PJ and Edwin for our INST326 final at the University of Maryland. This project allows a user to insert values and the machine learning model will 
the cost of the house and determine the quality of the deal. This is accomplished by downloading information off of redfin and pre-processing this data. From here, determined the appropraite model to use and implented it for the user input.

Run the main portion of the code:

  The result of our code was a graphical user interface that accepts different feature values. From here, these feature vaules are tested against our machine learning model and then a price is 
  predicted. In order to run this part of the code a user must type, python UI.py, use python3 if on mac when in the folder for the project. This will bring up a GUI which will have two dropdowns 
  and multiple empty boxes with labels. A user must choose the values for all no matter what for the code to run, except for the price. The price value is optional. When all information is   
  submitted the user must click the house price prediction button. From here, the machine learning model starts and will train the model and then predict the price. When the predicted price is 
  determined, two things could happen depending on if a price is given. If they do, it will show the predicted price, the inputed price, and will rate the deal. 
  If a price is not entered, then the predicted price range is shown.

How to run code in command line:

  In order to run the code in the command line, you must open the folder in the command line and then type python(3), 3 if on an mac, and then the file name
  for example you open the UI folder through cd yourpath/INST326Final/UI then you use python UI.py to run the UI file 

How to run the code and interpret:

  To run the code you can type python, python3 if you have a mac, and then the file name to run an file.
  The data cleaning file out put is formatted in a readable manner.
  The ML models display the average difference between the actual price. So if the output is 10,000, for a house of 200,000 the model will give a number between 210,000 and 190,000.
  For the GUI, the GUI displays a message. The message will depend on if the user adds a price. If they do, it will show the predicted price, the inputed price, and will rate the deal. 
  If a price is not entered, then the predicted price range is shown.

Sources:
  For ML:
  
1.4. Support Vector Machines. scikit. (n.d.-a). https://scikit-learn.org/stable/modules/svm.html This is the documentation for the machine learning algorithm, support vector machine. This algorithm was used while testing the accuracy for different algorithms. This webpage allowed us to accurately implement the model and test the results accuracy of the model against the different models.

Catboostclassifier. CatBoost. (n.d.). https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier This webpage is the documentation for the catboostclassifier. This is a library that has a ML model that is used in the program. This webpage was necessary to gain an understanding of how the model works and the requirements for it to work.

GeeksforGeeks. (2023, April 30). House price prediction using machine learning in Python. GeeksforGeeks. https://www.geeksforgeeks.org/house-price-prediction-using-machine-learning-in-python/ This page was used to get an understanding of how machine learning models are used for housing predictions and to determine the machine learning models that are best for housing predictions.

Ihre, A., &amp;  Engstrom, I. (n.d.). Predicting House prices with machine learning methods - diva. https://www.diva-portal.org/smash/get/diva2:1354741/FULLTEXT01.pdf This webpage was used to get an understanding of the process it takes to create a model to predict housing prices. It allowed us to understand what is necessary for the code and how to determine which features are best.

Sklearn.ensemble.randomforestregressor. scikit. (n.d.-b). https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html This is the webpage for the random forest regressor documentation. It is a linear regression model which uses multiple decision trees for one result. The webpage allowed us to implement the model accurately for our code.

Sklearn.linear_model.linearregression. scikit. (n.d.-c). https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html This webpages is the documentation for linear regression. This webpage gave us an understanding of how to implement linear regression in our model to determine its accuracy.

Sklearn.linear_model.Ridge. scikit. (n.d.-d). https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html This is the documentation for the ridge regression model. This webpage gave us an understanding of the model and how to implement it for our model in order to obtain accurate results.
      
  For GUI:
  
GeeksforGeeks. (2023, January 6). Create first GUI application using Python-Tkinter. GeeksforGeeks. https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/ Our group had little idea how to create a gui for the user to input feature data Our group decided to use Tkinter for building our GUI. This page gave us an understanding of how Tkinter works and how to create the gui and accept user input.

Graphical user interfaces with TK. Python documentation. (n.d.). https://docs.python.org/3/library/tk.html This webpage is the documentation for Tkinter and allowed us to understand what was allowed in Tkinter and how to use it properly for our gui.

  For User Input on GUI:

Fitzpatrick, M. (2023, September 13). Validate user input when creating apps with Tkinter and python. Python GUIs. https://www.pythonguis.com/tutorials/input-validation-tkinter/ This file outlined user inputs in Tkinter and allowed us to be able to allow and handle user data for our model. This was a necessary step because without it our project idea would not have worked.
Testing prediction model with user input.

Stack Overflow. (1965, December 1). https://stackoverflow.com/questions/58712891/testing-prediction-model-with-user-input We were struggling having the model run on the user input and the code given in the stackoverflow page was necessary to get it to function. The code is in our file and allows it to run how we desired.

  For Unit testing:



