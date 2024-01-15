import unittest
import sys
sys.path.append('../data/')

from logic import FindIndex
from logger import Logger
from logger import Loglevels

def LoadData(input_file):
    data = None
    with open(input_file) as datasource: 
        #data = datasource.readlines() 
        data=datasource.read().splitlines()
    return data

data = LoadData('./data/test_input.txt')
log_level = Loglevels.INFO.value
logger = Logger(log_level)


################ Unit tests ################

class TestStringMethods(unittest.TestCase):

    def test_load_data(self):
        self.assertEqual(len(data), 14)
        self.assertEqual(data, ['10','70','80','90','92','100','104','105','110','120','200','300','400','500'])
        logger.OK(f"test_load_data - finished")

    def test_range_match(self):
        ret, exact_match = FindIndex(data, 95, 10, logger)
        self.assertEqual(exact_match, False)
        self.assertEqual(ret['index'], [3,4,5,6])
        logger.OK(f"test_range_match - finished")


    def test_exact_match(self):
        self.assertEqual('foo'.upper(), 'FOO')
        logger.OK(f"test_exact_match - finished")

    def test_run_on_empty_list(self):
        ret, exact_match = FindIndex([], 95, 10, logger)
        self.assertEqual(ret['index'], [])
        self.assertEqual(ret['value'], [])
        self.assertEqual(exact_match, False)
        logger.OK(f"test_run_on_empty_list - finished")

    def test_run_on_small_list_without_match(self):
        ret, exact_match = FindIndex([1,200], 95, 10, logger)
        self.assertEqual(ret['index'], [])
        self.assertEqual(ret['value'], [])
        self.assertEqual(exact_match, False)
        logger.OK(f"test_run_on_small_list_without_match - finished")
    
    def test_run_on_small_list_with_match(self):
        ret, exact_match = FindIndex([1,95, 200], 95, 10, logger)
        self.assertEqual(ret['index'], 1)
        self.assertEqual(ret['value'], 95)
        self.assertEqual(exact_match, True)
        logger.OK(f"test_run_on_small_list_with_match - finished")

if __name__ == '__main__':
    unittest.main()