import unittest
import csv

# Import the module to test
from input import *
        
class TestInputCSV(unittest.TestCase):
        
    def test_read_csv(self):
        # Assuming the file '/home/wolf/files/file.csv' exists and has known content
        file_path = '/home/wolf/files/file.csv'
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            expected_rows = [row for row in csv_reader]
        
        #with self.assertLogs(level='INFO') as log:
        
            
        output_rows = input_csv.read_csv(file_path)
        
        self.assertEqual(output_rows, expected_rows)
                         
                         
                         
if __name__ == '__main__':
    unittest.main()