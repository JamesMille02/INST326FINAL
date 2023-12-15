import unittest
import pandas as pd
import os
import sys
from pandas.testing import assert_frame_equal
from contextlib import redirect_stdout
from contextlib import contextmanager
from io import StringIO
import tempfile
from pandas.testing import assert_frame_equal
from data_set_prep.data_cleaning import (combine_csv_files, 
                                        drop_unwanted_columns, is_null,
                                        property_type_values, 
                                        find_unique_cities,
                                        property_type_drop_rows,
                                        property_type_reclassification, 
                                        city_reclassification, 
                                        column_classification_check, hoa_prep,
                                        calc_price_per_sqft, lot_size_prep, 
                                        drop_null_rows)

@contextmanager
def captured_output():
    """Captures the printed statement from the methods in data_cleaning
    to compare to the expected value to ensure the method is functioning 
    properly.
    """

    #saves the output in StringIO instances
    new_out, new_err = StringIO(), StringIO()
    #gets the old instances of StringIO
    old_out, old_err = sys.stdout, sys.stderr
    try:
        #replaces the old string output with the new
        sys.stdout, sys.stderr = new_out, new_err
        #creates new StringIO() instances
        yield sys.stdout, sys.stderr
    finally:
        #saves the yielded out put as the old output
        sys.stdout, sys.stderr = old_out, old_err

class TestCSVFunctions(unittest.TestCase):
    def setUp(self):
        """creates an temp directory to hold files for testing purposes so 
        the files in the program are not effected.
        """

        #creates an instance of a temporary directory for testing 
        self.temp_dir = "test_dir"
        #creates the path to the temporary directory
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        """deletes the temp directory because it is no longer needed after 
        testing
        """

        #goes through the seperate files in the temp directory
        for file_name in os.listdir(self.temp_dir):
            #gets the complete path
            file_path = os.path.join(self.temp_dir, file_name)
            #removes the file through the path
            os.remove(file_path)
        #removes the temporary directory after testing
        os.rmdir(self.temp_dir)

    def test_combine_csv_files(self):
        """tests the combine csv file by creating a csv file in the temp 
        directory and calls the method to join them and checks if true
        """
        #creates test CSV files in the temporary directory
        test_csv = {"A": [1, 2, 3], "B": [4, 5, 6]}
        #adds a csv file  to the temp directory
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir, 
                                                        "test1.csv"), 
                                                        index=False)
        #adds a second csv file to the temp directory
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir, 
                                                        "test2.csv"), 
                                                        index=False)

        #adds a file for the combined csv to go into
        file_output = os.path.join(self.temp_dir, "combined_output.csv")
        #tests the combine_csv_files method by calling the temp directory
        #which holds the csv and the file which will hold the combined csv
        combine_csv_files(self.temp_dir, file_output)

        #check if the combined file exists
        self.assertTrue(os.path.exists(file_output))

    def test_drop_unwanted_columns(self):
        """tests the drop_unwanted_columns to ensure the columns that are 
        meant to be deleted are.
        """

        #creates test data
        test_csv_data = {"A": [1, 2, 3], "B": [4, 5, 6]}
        #adds the data to the csv  file
        test_csv = pd.DataFrame(test_csv_data)
        #determins the column to drop
        columns_dropped = ["B"]
        #calls the drop_unwanted_columns method to test it 
        result = drop_unwanted_columns(test_csv, columns_dropped)

        #check if the specified column is dropped
        self.assertNotIn("B", result.columns)

    def test_is_null_with_null_values(self):
        """tests to see if rows columns with null values are detectable through
        the is_null method"""

        #creates data
        test_csv = {"A": [1, 2, None], "B": [4, None, 6]}
        #saves it to the temp directory and in a temp file
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir,
                                                         "tests_null.csv"), 
                                                         index=False)

        #tests the is_null function with a file containing null values
        file_output = os.path.join(self.temp_dir, "tests_null.csv")
        #captures the output from is null
        with captured_output() as (out, err):
            is_null(file_output)

        #checks if the expected message is present in the printed output
        expected_output = f"Null value counts per column:"
        "\nA    1\nB    1\ndtype: int64"
        is_null_output = out.getvalue().strip()

        self.assertIn(expected_output, is_null_output)

    def test_is_null_without_null_values(self):
        """tests the is null values when there are no values to ensure that the
        is_null method works with and without null values
        """

        #creates test data
        test_csv = {"A": [1, 2, 3], "B": [4, 5, 6]}
        #saves the data in the temp directory in a temp file
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir, 
                                                        "tests_no_null.csv"), 
                                                        index=False)
        #saves the file path
        file_output = os.path.join(self.temp_dir, "tests_no_null.csv")
        #captures the output of the is_null method with the file path to
        #the temp directory
        with captured_output() as (out, err):
            is_null(file_output)
        # Check if the expected message is present in the printed output
        expected_output = "The CSV file does not contain any null values."
        no_null_output= out.getvalue().strip()

        self.assertIn(expected_output, no_null_output)

    def test_property_type_values(self):
        """tests to see if the property_type_values can identify and display all
        of the property_type_values
        """

        #creates a test list in a dictiionary holding the different property
        #types
        test_csv = {"PROPERTY TYPE": ["House", "Apartment", "House", 
                                           "Condo", "Apartment"]}
        #saves the data to a file in the temp directory
        pd.DataFrame(test_csv).to_csv(os.path.join
                                           (self.temp_dir,
                                            "tests_property_type.csv"), 
                                            index=False)

        #saves the file path 
        file_output = os.path.join(self.temp_dir, "tests_property_type.csv")
        #calls the property_type_values and saves the output
        with captured_output() as (out, err):
            property_type_values(file_output)
        #checks to see if the output is expected
        expected_output = "House        2\nApartment    2\nCondo        1"
        property_type_values_output = out.getvalue().strip()

        self.assertIn(expected_output, property_type_values_output)

    def test_property_type_reclassification(self):
        """makes the property_type_reclassification method is properly changing
        property types to the correct numeric values.
        """

        #creates temp csv
        test_csv = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        #created data
        data = {
            'PROPERTY TYPE': ['Single Family Residential', 'Townhouse', 
                              'Single Family Residential'],
            'Another Column': [1, 2, 3],
        }

        #creates a data frame fram with the data
        test_data = pd.DataFrame(data)
        #saves the data frame to the temp file
        test_data.to_csv(test_csv.name, index=False)
        #calls the property_type_reclassification on the temp file
        property_type_reclassification(test_csv.name)
        #reads the contents
        modified_data = pd.read_csv(test_csv.name)
        #expected mapping for the data
        expected_mapping = {
            'Single Family Residential': 1,
            'Townhouse': 2
        }
        #assigns the property types values for the expected results
        expected_values = test_data['PROPERTY TYPE'].map(expected_mapping)

        #determines if the values are equal
        pd.testing.assert_series_equal(modified_data['PROPERTY TYPE'], 
                                       expected_values)

    def test_find_unique_cities(self):
        """tests the find_unique_cities method in order to determine it can
        find each individual city.
        """

        #creates test data
        test_csv = {"CITY": ["City1", "City2", "City1", "City2", "City3"]}
        #saves the test data in the temp directory in a file
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir, 
                                                        "testing_cities.csv"), 
                                                        index=False)
        #saves the file path
        file_output = os.path.join(self.temp_dir, "testing_cities.csv")
        #saves the output of find_unique_city
        with captured_output() as (out, err):
            find_unique_cities(file_output)
        #checks if the expected message is present in the printed output
        expected_output = "['City1', 'City2', 'City3']"
        find_unique_cities_output = out.getvalue().strip()

        self.assertIn(expected_output, find_unique_cities_output)

    def test_property_type_drop_rows(self):
        """tests if the right columns are able to be dropped when using the 
        property_type_drop_rows method.
        """

        #created test data
        test_csv = {"PROPERTY TYPE": ["House", "Condo", 
                                           "Single Family Residential", 
                                           "Townhouse", "Apartment"]}
        #saves the test data in the temp directory
        pd.DataFrame(test_csv).to_csv(os.path.join
                                           (self.temp_dir, 
                                            "testing_property_type_drop.csv"), 
                                            index=False)

        #saves the path to the file holding the test data
        file_input = os.path.join(self.temp_dir, "testing_property_type_drop.csv")
        #calls the property_type_drop_rows method
        property_type_drop_rows(file_input)
        #reads the csv file
        modified_df = pd.read_csv(file_input)
        #assigns the values which are expected
        property_type_drop_rows_output = ["Single Family Residential", "Townhouse"]
        #sees if only the values in expected_values are present

        self.assertTrue(all(value in modified_df['PROPERTY TYPE'].values for 
                            value in property_type_drop_rows_output))
        #sees if it is the correct length
        self.assertEqual(len(modified_df), len(property_type_drop_rows_output))

    def test_city_reclassification(self):
        """tests if the cities gets numeric values for each unique city. This
        is done through the city reclassification method and is important 
        due to the fact that the models only accept numeric featuers
        """

        #creates test data
        test_csv_data = {"CITY": ["City1", "City2", "City1", "City3", "City2"]}
        #creates a file in the temp directory
        pd.DataFrame(test_csv_data).to_csv(os.path.join(self.temp_dir, 
                                                     "test_city_reclass.csv"),
                                                    index=False)

        #saves the path of the file in the temp directory
        file_path = os.path.join(self.temp_dir, 
                                  "test_city_reclass.csv")
        #calls the city classification method on the input file
        city_reclassification(file_path)
        #read the modified file and saves it
        city_reclassification_output = pd.read_csv(file_path)
        #defines the expected values
        expected_indices = [0, 1, 0, 2, 1]
        #checks to see if the indexes assigned are correct

        self.assertTrue(all(index == expected_index for index, expected_index 
                            in zip(city_reclassification_output['CITY'], 
                                   expected_indices)))


    def test_column_classification_check(self):
        """tests to see if the column classification method can determine the
        column types. This is important bc even if the values are numeric 
        the column types needs to be int or float or the model throughs errors.
        """

        #creates test  data
        test_csv = {"Column1": [3, 4, 5], "Column2": [4.0, 5.0, 6.0]}
        #saves the data to a file
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir, 
                                                "test_column_class_check.csv"), 
                                                index=False)

        #saves the path to the file in the temp directory
        file_path = os.path.join(self.temp_dir, 
                                  "test_column_class_check.csv")
        
        #opens the file
        with open(os.path.join(self.temp_dir, "test.txt"), 'w') as f:
            #saves the output from the method
            with redirect_stdout(f):
                non_numeric_columns = column_classification_check(file_path)
        #reads the file changes
        with open(os.path.join(self.temp_dir, "test.txt"), 'r') as f:
            column_classification_output = f.read()
        #assigns the expect value to the expected values
        expected_output = "All columns have numeric types (int or float)."

        #tests if the values are the same and if the non_numeric_columns list
        #is empty
        self.assertIn(expected_output, column_classification_output)
        self.assertEqual(non_numeric_columns, [])
    
    def test_calc_price_per_sqft(self):
        """checks if the calc_price_per_sqft method correctly calculates the
        price per square foot and handles null values.
        """

        #created test data
        test_data = pd.DataFrame({
            'PRICE': [200000, 300000, 250000],
            'SQUARE FEET': [1500, 1800, 2000],
        })
        #saves temp data in a csv
        test_data.to_csv(os.path.join(self.temp_dir, 
                                      'test_calc_price_per_sqft.csv'), 
                                      index=False)
        #gets the file path
        file_path = os.path.join(self.temp_dir, 'test_calc_price_per_sqft.csv')
        #calls the cal_price_per_sqft function on the temp file
        calc_price_per_sqft(file_path)
        #reads the temp  file
        calc_price_per_sqft_output = pd.read_csv(file_path)
        #calculates the price per square foot
        expected_values = test_data['PRICE'] / test_data['SQUARE FEET']
        expected_values.fillna(0, inplace=True)
        #sets the name of the expected series to match the modified series 
        expected_values.name = '$/SQUARE FEET'

        #checks if the calc_price_per_sqft has the correct output
        pd.testing.assert_series_equal(calc_price_per_sqft_output
                                       ['$/SQUARE FEET'], expected_values)

    def test_lot_size_prep(self):
        """tests if the lot_size_prep method correctly replaces null lot sizes
        with the square footage of the house.
        """

        #created test data
        lot_size_data = pd.DataFrame({
            'SQUARE FEET': [1500, 1800, 2000],
            'LOT SIZE': [3000, None, 2500],
        })
        #saves data in csv
        lot_size_data.to_csv(os.path.join(self.temp_dir, 
                                      'test_lot_size_prep.csv'), index=False)
        #saves file path of the test CSV
        file_path = os.path.join(self.temp_dir, 'test_lot_size_prep.csv')
        #calls the lot_size_prep function on the temp file
        lot_size_prep(file_path)
        #reads the data in the CSV
        calc_price_per_sqft_file = pd.read_csv(file_path)
        #expected data with null lot size replaced by square footage
        expected_data = pd.DataFrame({
            'SQUARE FEET': [1500, 1800, 2000],
            'LOT SIZE': [3000, 1800, 2500],  
        })

        #check if the lot_size_prep gives the right output
        assert_frame_equal(calc_price_per_sqft_file, expected_data, 
                           check_dtype=False)

    def test_hoa_prep(self):
        """tests if the hoa price assigns 0s to the none values and no other
        values. this is necassary because the model will not work with null 
        values
        """

        #creates test data
        test_csv = {"HOA/MONTH": [100, None, 150]}
        #saves the data to a temp file
        pd.DataFrame(test_csv).to_csv(os.path.join(self.temp_dir,
                                                         "test_hoa_prep.csv"), 
                                                         index=False)
        #saves the file path
        file_path = os.path.join(self.temp_dir, "test_hoa_prep.csv")
        #calls the hoa prep method
        hoa_prep(file_path)
        #reads the file and saves it 
        hoa_prep_result = pd.read_csv(file_path)
        #saves the expected values 
        expected_values = [100, 0, 150]
        #checks to see if the expected values are the same as what is in the
        #file

        self.assertListEqual(list(hoa_prep_result['HOA/MONTH']), 
                             expected_values)

    def test_drop_null_rows(self):
        """tests to determine if the correct rows are dropped during the 
        drop_null_rows method
        """
        #creates test data
        test_csv = {"BATHS": [2, None, 3, 1],
                          "SQUARE FEET": [1500, 1800, None, 2000], 
                          "LOT SIZE": [3000, 2500, 2000, None]}
        #saves a temp file in the temp directory
        test_path = os.path.join(self.temp_dir, "test_drop_null_rows.csv")
        #creates the file with the temp data
        pd.DataFrame(test_csv).to_csv(test_path, index=False)
        #calls the drop_null_method on the created temp file
        drop_null_rows(test_path)
        #reads the file
        null_output = pd.read_csv(test_path)
        #assigns the expected result
        expected_data = {"BATHS": [2.0], "SQUARE FEET": [1500.0], 
                         "LOT SIZE": [3000.0]}
        #assigns the expected data to a dataframe for comparison
        expected_df = pd.DataFrame(expected_data)

        #checks if file and expected df are the same
        assert_frame_equal(null_output, expected_df, check_dtype=False)


if __name__ == '__main__':
    unittest.main()



