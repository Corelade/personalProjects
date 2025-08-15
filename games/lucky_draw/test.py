import unittest
from lucky_draw import *
from unittest.mock import patch


class TestNumericInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['5'])
    def test_in_range_number(self, mock_input):
        'This correctly selects a number in the range and tests it'
        resp = get_numeric_input('Enter a number between 5-9: ')
        self.assertEqual(resp, 5)
    
    @patch('builtins.input', side_effect=['0', 'a', '10', '6'])
    def test_multi_number(self, mock_input):
        'This uses the next number as result if the current number fails'
        resp = get_numeric_input('Enter a number between 5-9: ')
        self.assertEqual(resp, 6)
    
    @patch('builtins.input', side_effect=[7])
    def test_not_equal_number(self, mock_input):
        'This passes if the input is not equal to output'
        resp = get_numeric_input('Enter a number between 5-9: ')
        self.assertNotEqual(resp, 6)
        
        
if __name__ == '__main__':
    unittest.main()