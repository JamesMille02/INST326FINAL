def graph(data, column1, column2):
    """Creates a graph by using two columns in order to compare values to 
    establish a relationship between columns
    
    Args:
        data (DataFrame): A pandas DataFrame containing the data.
        column1(str): a string representing a column which data will be used in 
            the graph.
        column2(str): a string representing a column which data will be used in 
            the graph.
    
    Output:
        A graph where the x and y are two values and data points are
            plotted accross to view linear regression.
    """
    plt.plot(data[column1], data[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f"Line Graph of {column1} vs {column2}")
    plt.show()
    
    pass

def heatmap(csv_file):
    """Creates a heatmap to visualize the correlation between columns in a dataset.

    Args:
        csv_file(str): string representing the file name which contains the 
            file of data.

    Output:
        Displays a heatmap with color shades representing the correlation strengths between columns.
    
    """
    data = pd.read_csv(csv_file)
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.title("Heatmap of Correlations")
    plt.show()
    
    pass

def histogram(data, column1, column2 ):
    """a histogram to show establish the frequency of numeric values.

    Args:
        data (DataFrame): A pandas DataFrame containing the data.
        column1(str): a string representing a column which data will be used in 
            the histogram.
        column2(str): a string representing a column which data will be used in 
            the histogram.

    Output:
        Histogram which contains plotted data points of a column.
    
    """
    pass

def scatterplot(data, column1, column2):
    """shows a scatter plot to establish relationship between columns.

    Args:
        data (DataFrame): A pandas DataFrame containing the data.
        column1(str): a string representing a column which data will be used in 
            the scatterplot.
        column2(str): a string representing a column which data will be used in 
            the scatterplot.
    
    Output:
        A scatter plot which shows the correlation between rows.
    """
    pass
