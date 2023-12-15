import unittest
import pandas as pd
import os
import unittest.mock

from data_set_prep.beds_prediction import compute_null_bed

class TestComputeNullBed(unittest.TestCase):
    def setUp(self):
        #created csv data
        data = {
            'BEDS': [2, 3, 4, None, 2],
            'PROPERTY TYPE': ['Single Family Residential', 'Condo', 'Townhouse',
                               'Single Family Residential', 'Condo'],
            'CITY': ['Bethesda', 'Annapolis', 'Bethesda', 'Annapolis',
                      'Bethesda'],
            'ZIP OR POSTAL CODE': ['20814', '21777', '20814', '21777', '20814'],
            'PRICE': [500000, 600000, 700000, 800000, 550000],
            'LATITUDE': [38.984654, 38.978939, 38.989674, 
                         38.978939, 38.984654],
            'LONGITUDE': [-77.094709, -76.532652, -77.098509, 
                          -76.532652, -77.094709]
        }

        self.test_null_bed_file = "test_compute_null_bed.csv"
        self.df = pd.DataFrame(data)
        self.df.to_csv(self.test_null_bed_file, index=False)

    def test_compute_null_bed(self):
        """computes if the compute_null_beds model determines the correct number
        of beds.
        """
        #calls compute_null_bed on the file holding the data
        compute_null_bed(self.test_null_bed_file)
        #reads the file and saves the contents
        read_file = pd.read_csv(self.test_null_bed_file)
        
        #ensures there are no null values
        self.assertFalse(read_file['BEDS'].isnull().any())
        
        #checks if the values are correct
        self.assertListAlmostEqual(read_file['BEDS'].tolist(), 
                                   [2, 3, 4, 3, 2], delta=0.1)

    def tearDown(self):
        #removes the temp file
        os.remove(self.test_null_bed_file)

    def assertListAlmostEqual(self, list1, list2, delta):
        """determines if lists are equal lengths and the numbers are the same
        in the list.
        
        Args:
            list1(list): contains data of beds
            list2(list): contains list of beds
        """

        #checks if equal length
        self.assertEqual(len(list1), len(list2))
        #iterates of the lists
        for a, b in zip(list1, list2):
            #determines if the numbers are equal
            self.assertAlmostEqual(a, b, delta=delta)

if __name__ == '__main__':
    unittest.main()
