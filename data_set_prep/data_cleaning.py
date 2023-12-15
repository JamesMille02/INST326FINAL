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
    #gets the csv files in the folder
    csv_files = [file for file in os.listdir(input_folder)]
    
    #empty list created
    joined_data = []
    
    #searches for all files in the folder
    for csv_file in csv_files:
        #joins the folder  and the csv_file
        file_join = os.path.join(input_folder, csv_file)
        #reads the files in the folder
        read_data = pd.read_csv(file_join)
        #appends the read data in the joined data
        joined_data.append(read_data)
    
    #concats this data together in a dataframe
    combined_data = pd.concat(joined_data, ignore_index=True)
    
    #combines to a csv
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
    #drops all files that are entered given
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

    #reads the csv_file
    df = pd.read_csv(csv_file)
    #gets the sum of null values in a column
    null_values = df.isnull().sum()

    #checks if over 1 null
    if null_values.sum() > 0:
        #prints the null values for each column
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

    #reads the csv_file
    df = pd.read_csv(csv_file)
    #counts total property types 
    property_type = df["PROPERTY TYPE"].value_counts()
    #prints the type and the count
    print(property_type)

def find_unique_cities(csv_file):
    """Find unique values in the 'CITY' column of the given CSV file.

    Args:
        csv_file (str): Path to the CSV file.

    Prints:
        unique city: List of unique values in the 'CITY' column.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Extract unique values from the 'CITY' column
    unique_cities = df['CITY'].unique().tolist()

    print(unique_cities)

def property_type_drop_rows(csv_file):
    """Drops the unwanted property types row. This is because the scope of the 
    project only contains the home type values.

    Args:
        csv_file: the file path to the csv file that contains the property
        type values.
    
    Yields:
        Specified rows are dropped depending on their Property Type value
    """

    #reads the csv_file
    df = pd.read_csv(csv_file)
    #specifies the columns we want to keep
    values_to_keep = df[df['PROPERTY TYPE'].isin(['Single Family Residential',
                                                   'Townhouse' ])]
    #saves to csv_file
    values_to_keep.to_csv(csv_file, index=False)

def property_type_reclassification(csv_file):
    """Turns the two property type columns values into numeric values because the 
    machine learning model only accepts numeric values

    Args:
        csv_file: the file path to the csv file that contains the property
        type values. 

    Yields:
        Edits the CSV file by changing single family residential values to 1
            and townhouse to 2
    """

    #reads csv_file
    df = pd.read_csv(csv_file)
    #sets the property types to numeric values
    property_mapping = {
        'Single Family Residential': 1,
        'Townhouse': 2
    }
    #changes the property types to the corresponding number
    df['PROPERTY TYPE'] = df['PROPERTY TYPE'].map(property_mapping)
    #saves it to the csv
    df.to_csv(csv_file, index=False)


def city_reclassification(csv_file):
    """Turns the city strings into numeric values in order to run the machine
    learning model.

    Args:
        csv_file: the file path to the csv file that contains the city
        column.  

    Yields:
        Gives each city a numerical index and changes the city name string
            to the numerical index value
    """

    #reads the csv_file
    df = pd.read_csv(csv_file)
    #finds all cities
    unique_cities = df['CITY'].unique()
    #goes through each individual city in the unique cities array and saving 
    #the number it comes up as in the array if it unique
    city_mapping = {city: index for index, city in enumerate(unique_cities)}
    #changes the city to the number corresponding
    df['CITY'] = df['CITY'].map(city_mapping)
    #saves to the csv file
    df.to_csv(csv_file, index=False)

def column_classification_check(csv_file):
    """Checks the column types of each column to ensure they are all int.

    Args:
        csv_file (str): the file path to the CSV file used in the machine
        learning model.

    Returns:
        list: A list of strings representing the names of columns that are
        not of type int. If all columns are of type int, it prints a statement
        indicating this.
    """

    #reads csv_file
    df = pd.read_csv(csv_file)

    #selects all types of columns that are not int or float type
    non_numeric_columns = df.select_dtypes(exclude=['int',
                                                     'float']).columns.tolist()

    if not non_numeric_columns:
        print("All columns have numeric types (int or float).")
    else:
        print("Columns with non-numeric types:", non_numeric_columns)
        
    return non_numeric_columns


def hoa_prep(csv_file):
    """Changes all null values in the hoa column to zero.

    Args:
        csv_file(str): the name of the file that contains the hoa column

    Yields:
        An updated csv file where all null values in the hoa column are 0
    """

    #reads the cssv
    df = pd.read_csv(csv_file)
    #fills the HOA/MONTH with a 0 if it is NA
    df['HOA/MONTH'] = df['HOA/MONTH'].fillna(0)
    #saves tot the csv
    df.to_csv(csv_file, index=False)


def calc_price_per_sqft(csv_file):
    """Calculates the price per a square feet of a house by dividing the sqft
    by the price and adding this to the csv file.

    Args:
        csv_file(str): file name of the file that contains the price per a sqft
            column.
    
    Yields:
        An updated csv file where the null values in the price per sqft column
            are now the calculated values
    """
    
    #reads the csv file
    df = pd.read_csv(csv_file)
    #price per a square foot
    df['$/SQUARE FEET'] = df['PRICE'] / df['SQUARE FEET']
    #replace null values with this value
    df['$/SQUARE FEET'].fillna(0, inplace=True)

    #saves to the csv
    df.to_csv(csv_file, index=False)


def lot_size_prep(csv_file):
    """Changes all lot sizes that are null to the sqft value of the house

    Args:
        csv_file(str): file name of the file that contains the lot size column

    Yields:
        An updated csv file where all null lot_sizes are updated to the sqft
        of the house
    """

    #reads the csv_file
    df = pd.read_csv(csv_file)
    #replace null values in the 'lot_size' column with the 'sqft' value
    df['LOT SIZE'].fillna(df['SQUARE FEET'], inplace=True)
    #saves to the csv_file
    df.to_csv(csv_file, index=False)

def drop_null_rows(csv_file):
    """Drops the rows with null values in the BATHS, SQUARE FEET, and LOT SIZE
    columns.

    Args:
        csv_file(str): file name of the file that contains the lot size column

    Yields:
        An updated csv value where the rows with missing values rows are not
            present. Drops a total of 277 rows.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Drop rows with any null values
        df = df.dropna()

        # Save the modified DataFrame back to the CSV file
        df.to_csv(csv_file, index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


#example calls
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
#property_type_reclassification(input_file)

#column_classification_check(input_file)

#hoa_prep(input_file)

#calc_price_per_sqft(input_file)

#lot_size_prep(input_file)

#drop_null_rows(input_file)

#csvfile = 'final_data_set.csv'
#find_unique_cities(csvfile)