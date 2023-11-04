import pandas as pd
import os

def combine_csv_files(input_folder, output_file):
    """This metod takes multiple csv files and combines them into one. Prints 
    the number of files combined into the output file.

    Args:
        input_folder: the path to a folder containing csv files
        output_file: the file path you want the csvs to be written into
    
    Prints:
        The amount of files saved into the name of the output folder
    """
    csv_files = [file for file in os.listdir(input_folder)]
    
    joined_data = []
    
    for csv_file in csv_files:
        file_join = os.path.join(input_folder, csv_file)
        read_data = pd.read_csv(file_join)
        joined_data.append(read_data)
    
    combined_data = pd.concat(joined_data, ignore_index=True)
    
    combined_data.to_csv(output_file, index=False)
    print(f"Combined {len(csv_files)} CSV files into {output_file}")

def drop_unwanted_columns(csv_file, columns_to_drop):
    """Takes the csv file and drops specified columns.

    Args: 
        data: the file path that you want to drop the columns from
        columns_to_drop: a list of columns that you want to drop
    
    Returns:
        returns the altered data set without the dropped columns
    """
    data = csv_file.drop(columns=columns_to_drop, errors='ignore')
    return data


def is_null(csv_file):
    """Takes a csv file and checks if any of the values are null for each 
    column.

    Args:
        file path to the csv file that you want to check the null values for the
        columns.

    Prints:
        The columns alongside the number of null values.
    """

    df = pd.read_csv(csv_file)
    null_values = df.isnull().sum()

    if null_values.sum() > 0:
        print(f"Null value counts per column:\n{null_values}")
  
    else:
        print("The CSV file does not contain any null values.")

def property_type_values(csv_file):
    """Counts the different types of property types value.

    Args:
        csv_file: the path to the csv file that contains the property type
        values.
    
    Prints:
        The different property types and the count of each in the column
    """

    df = pd.read_csv(csv_file)
    property_type = df["PROPERTY TYPE"].value_counts()
    print(property_type)

def property_type_drop_rows(csv_file):
    """Drops the unwanted property types row. This is because the scope of the 
    project only contains the home type values.

    Args:
        csv_file: the file path to the csv file that contains the property
        type values.
    """

    df = pd.read_csv(csv_file)
    values_to_keep = df[df['PROPERTY TYPE'].isin(['Single Family Residential',
                                                   'Townhouse' ])]
    values_to_keep.to_csv(csv_file, index=False)

def property_type_reclassification(csv_file):
    """Turns the two property type columns values into numeric values because the 
    machine learning model only accepts numeric values

    Args:
        csv_file: the file path to the csv file that contains the property
        type values. 

    Output:
        Edits the CSV file by changing single family residential values to 1
            and townhouse to 2
    """
    df = pd.read_csv(csv_file)
    property_mapping = {
        'Single Family Residential': 1,
        'Townhouse': 2
    }
    df['PROPERTY TYPE'] = df['PROPERTY TYPE'].map(property_mapping)
    df.to_csv(csv_file, index=False)


def city_reclassification(csv_file):
    """Turns the city strings into numeric values in order to run the machine
    learning model.

    Args:
        csv_file: the file path to the csv file that contains the city
        column.  

    Output:
        Gives each city a numerical index and changes the city name string
            to the numerical index value
    """
    df = pd.read_csv(csv_file)
    unique_cities = df['CITY'].unique()
    city_mapping = {city: index for index, city in enumerate(unique_cities)}
    df['CITY'] = df['CITY'].map(city_mapping)
    df.to_csv(csv_file, index=False)


def column_classification_check(csv_file):
    """Checks the column types of each columns to ensure they are all int or 
    an error will be thrown by the sklearn library while running the machine
    learning model.

    Args:
        csv_file(str): the file path to the csv file that is used in the machine
        learning model.

    Return:
        A list of strings that represent the names of columns that are 
            not int and if there are none it will print a statement representing
            this fact.
    """
    pass

def column_type_to_int(columns):
    """changes all non int column types to in by accepting the list returned
    from the column classification check method and changing those columns to 
    integer representation. This is necessary for the machine learning model.

    Args: 
        columns(list): a list of column names that are not of int type

    Output:
        an updated data set where all specified columns are of type int or float
    """
    pass

def hoa_prep(csv_file):
    """Changes all null values in the hoa column to zero.

    Args:
        csv_file(str): the name of the file that contains the hoa column

    Output:
        An updated csv file where all null values in the hoa column are 0
    """
    pass

def calc_price_per_sqft(csv_file):
    """Calculates the price per a square feet of a house by dividing the sqft
    by the price and adding this to the csv file.

    Args:
        csv_file(str): file name of the file that contains the price per a sqft
            column.
    
    Output:
        An updated csv file where the null values in the price per sqft column
            are now the calculated values
    """
    pass

def lot_size_prep(csv_file):
    """Changes all lot sizes that are null to the sqft value of the house

    Args:
        csv_file(str): file name of the file that contains the lot size column

    Output:
        An updated csv file where all null lot_sizes are updated to the sqft
        of the house
    """
    pass





#example call for drop_unwanted_colums
input_file = 'feature_prediction.csv'
#input_data = pd.read_csv(input_file)
#columns_to_remove = ['YEAR BUILT']
#cleaned_data = drop_unwanted_columns(input_data, columns_to_remove)
#cleaned_data.to_csv(input_file, index=False)

#example call for is_null
#is_null(input_file)

#example call for property_type_values
#property_type_values(input_file)

#example call for property_type_reclassification
#input_csv_file = 'original_data.csv'  # Replace with your input CSV file path
#property_type_drop_rows(input_file)

#city_reclassification(input_file)
property_type_reclassification(input_file)