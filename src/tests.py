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

    def test_duplicated_items_no_match(self):
        ret, exact_match = FindIndex([1,95,95,95,200], 120, 10, logger)
        self.assertEqual(exact_match, False)
        self.assertEqual(ret['index'], [])
        self.assertEqual(ret['value'], [])
        logger.OK(f"test_duplicated_items_no_match - finished")

    def test_duplicated_items_exact_match(self):
        test_data = [1,95,95,95,200]
        target_value = 95
        ret, exact_match = FindIndex(test_data, target_value, 10, logger)
        logger.DEBUG(f"{ret['index']}")
        logger.DEBUG(f"{ret['value']}")
        self.assertEqual(exact_match, True)
        self.assertEqual(test_data[ret['index']], target_value)
        self.assertEqual(test_data[ret['index']], ret['value'])
        self.assertEqual(ret['value'], target_value)
        logger.OK(f"test_duplicated_items_exact_match - finished")

    def test_duplicated_items_range_match(self):
        test_data = [1,95,95,95,200]
        target_value = 100
        ret, exact_match = FindIndex(test_data, target_value, 10, logger)
        logger.DEBUG(f"{ret['index']}")
        logger.DEBUG(f"{ret['value']}")
        self.assertEqual(exact_match, False)
        self.assertEqual(ret['index'], [1,2,3])
        self.assertEqual(ret['value'], [95,95,95])
        logger.OK(f"test_duplicated_items_exact_match - finished")


if __name__ == '__main__':
    unittest.main()