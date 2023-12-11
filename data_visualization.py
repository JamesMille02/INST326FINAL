# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

# Define a function to create a scatter plot
def graph(data, column1, column2):
    """
    Creates and displays a scatter plot for two specified columns from the given DataFrame.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    column1 (str): The name of the first column to be plotted on the x-axis.
    column2 (str): The name of the second column to be plotted on the y-axis.
    """
    plt.figure(figsize=(10,5))  # Set the figure size for the plot
    plt.scatter(data[column1], data[column2], alpha=0.5)  # Create a scatter plot
    plt.xlabel(column1)  # Set the label for the x-axis
    plt.ylabel(column2)  # Set the label for the y-axis
    plt.title(f"Scatter Plot of {column1} vs {column2}")  # Set the title of the plot

    formatter = ticker.StrMethodFormatter('{x:,.0f}')  # Format the x-axis tick labels
    plt.gca().xaxis.set_major_formatter(formatter)  # Apply the formatter to the x-axis

    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust the layout
    plt.show()  # Display the plot

# Define a function to create a heatmap
def heatmap(csv_file, columns):
    """
    Reads a CSV file, selects specified columns, and creates a heatmap of their correlations.

    Parameters:
    csv_file (str): The file path to the CSV file.
    columns (list): List of columns to include in the correlation heatmap.
    """
    data = pd.read_csv(csv_file)  # Read the CSV file
    selected_data = data[columns]  # Select the specified columns
    correlation_matrix = selected_data.corr()  # Calculate the correlation matrix
    
    plt.figure(figsize=(12,8))  # Set the figure size for the heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='viridis')  # Create a heatmap with annotations
    plt.title("Heatmap of Correlations for Selected Variables")  # Set the title of the heatmap
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.yticks(rotation=45)  # Rotate y-axis labels
    plt.tight_layout()  # Adjust the layout
    plt.show()  # Display the heatmap

# Load the data
data = pd.read_csv('final_data_set.csv')

# Specify columns to include in the heatmap
columns_to_include = ['PRICE', 'BEDS', 'BATHS', 'SQUARE FEET', 'LOT SIZE']

# Define a function to create a histogram
def histogram(data, column, max_value):
    """
    Creates and displays a histogram for a specified column in the DataFrame.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    column (str): The name of the column to create a histogram for.
    max_value (int): The maximum value for the histogram range.
    """
    filtered_data = data[data[column] <= max_value]  # Filter the data based on the max_value
    
    plt.figure(figsize=(10,5))  # Set the figure size for the histogram
    sns.histplot(filtered_data[column], bins=range(0, max_value+1), kde=False)  # Create a histogram
    plt.xlabel(column)  # Set the label for the x-axis
    plt.ylabel('Frequency')  # Set the label for the y-axis
    plt.title(f"Histogram of {column} up to {max_value}")  # Set the title of the histogram
    plt.xticks(range(0, max_value+1))  # Set the x-axis ticks
    plt.tight_layout()  # Adjust the layout
    plt.show()  # Display the histogram

# File path for the dataset
file_path = 'final_data_set.csv'
data = pd.read_csv(file_path)

# Create and display a scatter plot
graph(data, 'PRICE', 'SQUARE FEET')
# Create and display a histogram
histogram(data, 'BEDS', 10)
# Create and display a heatmap
heatmap('final_data_set.csv', columns_to_include)

pass
