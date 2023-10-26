import os
import csv
import pandas as pd
import glob


def combine_csv_files(input_folder, output_file):
    # List all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder)]
    
    if not csv_files:
        print("No CSV files found in the input folder.")
        return
    
    # Initialize an empty list to store DataFrames
    data_frames = []
    
    # Loop through CSV files and read them into DataFrames
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        data = pd.read_csv(file_path)
        data_frames.append(data)
    
    # Concatenate the DataFrames into a single DataFrame
    combined_data = pd.concat(data_frames, ignore_index=True)
    
    # Save the combined data to the output CSV file
    combined_data.to_csv(output_file, index=False)
    print(f"Combined {len(csv_files)} CSV files into {output_file}")


file_path = "final_data_set.csv"  # Replace with the path to your CSV file
data = pd.read_csv(file_path)
data.head()






