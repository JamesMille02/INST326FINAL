import pandas as pd
import os

def combine_csv_files(input_folder, output_file):
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

def drop_unwanted_columns(data, columns_to_drop):
    data = data.drop(columns=columns_to_drop, errors='ignore')
    return data


def is_null(input_file):
    df = pd.read_csv(input_file)
    null_values = df.isnull().sum()

    if null_values.sum() > 0:
        print(f"Null value counts per column:\n{null_values}")
  
    else:
        print("The CSV file does not contain any null values.")

def property_type_reidentification(data):
    pass

def city_reidentification(data):
    pass

def column_classification_chec(data):
    pass

def hoa_prep(data):
    pass

def lot_size_prep(data):
    pass

def calc_price_per_sqft(data):
    pass



#example call for drop_unwanted_colums
#input_file = 'feature_prediction.csv'
#input_data = pd.read_csv(input_file)
#columns_to_remove = ['YEAR BUILT']
#cleaned_data = drop_unwanted_columns(input_data, columns_to_remove)
#cleaned_data.to_csv(input_file, index=False)

#example call for is_null
#is_null(input_file)