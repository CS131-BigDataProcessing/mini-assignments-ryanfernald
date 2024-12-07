import unittest
import pandas as pd
from validate_functions import validate_victim_data
from stats_function import calculate_age_statistics

class TestStatsFunction(unittest.TestCase):
    def test_calculate_age_statistics_valid_data(self):
        data = {'Vict Age': [25, 30, 40, 50]}
        df = pd.DataFrame(data)
        
        stats = calculate_age_statistics(df)
        
        self.assertEqual(stats['mean_age'], 36.25)
        self.assertEqual(stats['median_age'], 35.0)

    def test_calculate_age_statistics_edge_case(self):
        data = {'Vict Age': [25]}
        df = pd.DataFrame(data)
        
        stats = calculate_age_statistics(df)
        
        self.assertEqual(stats['mean_age'], 25)
        self.assertEqual(stats['median_age'], 25)

class TestValidateFunctions(unittest.TestCase):
    def test_validate_victim_data_invalid_sex_datatype(self):
        data = {'Vict Sex': [123, 'F', None], 'Vict Age': [25, 30, 40]}
        df = pd.DataFrame(data)
        
        validation_results = validate_victim_data(df)
        
        self.assertEqual(validation_results['invalid_sex_count'], 2)  # 123 and None are invalid

    def test_validate_victim_data_valid_data(self):
        data = {'Vict Sex': ['M', 'F', 'M'], 'Vict Age': [25, 30, 40]}
        df = pd.DataFrame(data)
        
        validation_results = validate_victim_data(df)
        
        self.assertEqual(validation_results['invalid_sex_count'], 0)
        self.assertEqual(validation_results['invalid_age_count'], 0)

if __name__ == '__main__':
    unittest.main()