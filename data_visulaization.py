import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

def graph(data, column1, column2):
    plt.figure(figsize=(10,5))
    plt.scatter(data[column1], data[column2], alpha=0.5)
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f"Scatter Plot of {column1} vs {column2}")

    formatter = ticker.StrMethodFormatter('{x:,.0f}')
    plt.gca().xaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def heatmap(csv_file, columns):
    selected_data = data[columns]
    correlation_matrix = selected_data.corr()
    
    plt.figure(figsize=(12,8))
    sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
    plt.title("Heatmap of Correlations for Selected Variables")
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.show()

data = pd.read_csv('final_data_set.csv')

columns_to_include = ['PRICE', 'BEDS', 'BATHS', 'SQUARE FEET', 'LOT SIZE']

def histogram(data, column, max_value):
    filtered_data = data[data[column] <= max_value]
    
    plt.figure(figsize=(10,5))
    sns.histplot(filtered_data[column], bins=range(0, max_value+1), kde=False)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f"Histogram of {column} up to {max_value}")
    plt.xticks(range(0, max_value+1))
    plt.tight_layout()
    plt.show()

file_path = 'final_data_set.csv'
data = pd.read_csv(file_path)

graph(data, 'PRICE', 'SQUARE FEET')
histogram(data, 'BEDS', 10)
heatmap('final_data_set.csv', columns_to_include)

pass
