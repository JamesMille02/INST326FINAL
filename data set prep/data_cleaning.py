import pandas as pd
import os

def combine_csv_files(input_folder, output_file):
    """This metod takes multiple csv files and combines them into one. Prints 
    the number of files combined into the output file.

    Args:
        input_folder: the path to a folder containing csv files
        output_file: the file path you want the csvs to be written into
    
    Returned
    """
    csv_files = [file for file in os.listdir(input_folder)]
    
    if not csv_files:
        print("No CSV files found in the input folder.")
        return
    
    data_frames = []
    
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        data = pd.read_csv(file_path)
        data_frames.append(data)
    
    combined_data = pd.concat(data_frames, ignore_index=True)
    
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
    """Takes a csv file and checks if any of the 
    """
    df = pd.read_csv(csv_file)
    null_values = df.isnull().sum()

    if null_values.sum() > 0:
        print(f"Null value counts per column:\n{null_values}")
  
    else:
        print("The CSV file does not contain any null values.")

def property_type_values(csv_file):
    df = pd.read_csv(csv_file)
    property_type = df["PROPERTY TYPE"].value_counts()
    print(property_type)

def property_type_drop_rows(csv_file):
    df = pd.read_csv(csv_file)
    values_to_keep = df[df['PROPERTY TYPE'].isin(['Single Family Residential', 'Townhouse' ])]
    values_to_keep.to_csv(csv_file, index=False)
    print(f"Filtered data saved to {csv_file}")

def property_type_reclassification(csv_file):
    pass

def city_reclassification(data):
    pass

def column_classification_check(data):
    pass

def hoa_prep(data):
    pass

def lot_size_prep(data):
    pass

def calc_price_per_sqft(data):
    pass



#example call for drop_unwanted_colums
input_file = 'feature_prediction.csv'
#input_data = pd.read_csv(input_file)
#columns_to_remove = ['YEAR BUILT']
#cleaned_data = drop_unwanted_columns(input_data, columns_to_remove)
#cleaned_data.to_csv(input_file, index=False)

#example call for is_null
is_null(input_file)

#example call for property_type_values
#property_type_values(input_file)

#example call for property_type_reclassification
#input_csv_file = 'original_data.csv'  # Replace with your input CSV file path
#property_type_drop_rows(input_file)