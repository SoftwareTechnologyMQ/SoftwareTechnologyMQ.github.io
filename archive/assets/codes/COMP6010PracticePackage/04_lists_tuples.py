from cmath import log
from distutils.log import Log
from gettext import find
from random import random
import unittest
import math

def is_none(list):
    """
    Return true if the past list is None, false otherwise.
    """
    None

def is_empty(data):
    """
    Return true if the past list is empty or None, false otherwise.
    """
    None

def length(data):
    """
    Return the length of the list. 
    If the list is invalid (None), return -1.
    """
    None

def first_item(data):
    """
    Return the first item in the list. 
    If the list is invalid (None), return -1.
    """
    None

def sum(data):
    """
    Return the sum of all the items in the list.
    If the list is invalid, return -1
    """
    None

def count_even(data):
    """
    Return the number of even items in the list.
    If the list is invalid, return -1
    """
    None

def find_min(data):
    """
    Return the smallest number in the list.
    If the list is invalid, return None
    """
    None

def find_min_max(data):
    """
    Return the smallest number in data and then the
    largest number in data.
    If the list is invalid, return None
    """
    None

def all_positive(data):
    """
    Return true if all items in data are positive, false otherwise.
    """
    None

def atleast_one_divisible(data, n):
    """
    Return true if there exists one or more number in n that is divisible by n.
    n is a non-zero value.
    """
    None

def sum_even(data):
    """
    Return the sum of all even items in the list.
    If the list is invalid, return None
    """
    None

def add_even(data):
    """
    Return a list of all even items in the list.
    If the list is invalid, return an empty list
    """
    None

def power_indices(data, start, end):
    """
    Set all the values in the range [start, end) to the power of themselves.
    If data is invalid, return None
    """
    None

def power_indices_2(data, start, end):
    """
    Create an innstance copy of the values in 
    data and set all the values in the 
    range [start, end) to the power of themselves.
    If data is invalid, return None
    """
    None

def is_descending(data):
    """
    Return true if data is sorted is strtictly descending order, false otherwise.
    If data is invalid, return False
    """
    None

def mutually_reverse(a, b):
    """
    Return true if a and b are mutually reverse, false otherwise.
    Return false if either of the list/tuple passed is None
    """
    None

def all_unique(data):
    """
    Return true if all items in data are unique, false otherwise.
    If data is invalid, return False
    """
    None

def all_sublists_same_length(data):
    """
    Return true if all sublists in data are of the same length, false otherwise.
    If data is invalid, return False
    """
    None

def sum_sublists(data):
    """
    Return a list containing the length of every sublist.
    If data is None, return an empty list.
    """
    None

def all_descending(data):
    """
    Return true if the whole list/tuple is strictly descending, false otherwise.
    For example [(10, 7, 5), (3, 2, 1)] would be descending
    but [[10, 7, 6], [4], [5, 1]] would not be adescending
    since 5 > 4.
    """
    None

class Tester(unittest.TestCase):
    
    def setUp(self):
        self.list_empty = []
        self.list_taxi = [10, 70, 20, 90]
        self.list_neg_pos = [10, -5, 14, -8, 21]
        self.list_descending = [9, 8, 3, -4, -5, -17]
        self.list_ascending = [-17, -5, -4, 3, 8, 9]
        self.list_same_size = [[10, 70, 20, 90],
                               [-10, -70, -20, -90],
                               [9, 8, -5, -17],
                               [20, 32, 45, 70]]
        
        self.tuple_neg_taxi = (-10, -70, -20, -90)
        self.tuple_even = (4, -2, 8, 20, 14, 100)
        self.tuple_non_unique = (4, 10, 70, 4, 5, 70, 70)
        self.tuple_list = ([], [], [10, 70, 20, 90],
                           [9, 8, 7, 6, 5, 4, -1, -2], 
                           [], [20, 22],
                           [10, 70, 20, 90, 30, 80, 70],
                           [], [20, 32, 45, 70])
    
    def test_is_none(self):
        self.assertTrue(is_none(None))
        self.assertFalse(is_none(self.list_empty))
        self.assertFalse(is_none(self.list_taxi))
        self.assertFalse(is_none(self.list_neg_pos))
        self.assertFalse(is_none(self.list_descending))
        self.assertFalse(is_none(self.list_ascending))
        self.assertFalse(is_none(self.list_same_size))
        self.assertFalse(is_none(self.tuple_neg_taxi))
        self.assertFalse(is_none(self.tuple_even))
        self.assertFalse(is_none(self.tuple_non_unique))
        self.assertFalse(is_none(self.tuple_list))
        
    def test_is_empty(self):
        self.assertTrue(is_empty(None))
        self.assertTrue(is_empty(self.list_empty))
        self.assertFalse(is_empty(self.list_taxi))
        self.assertFalse(is_empty(self.list_neg_pos))
        self.assertFalse(is_empty(self.list_descending))
        self.assertFalse(is_empty(self.list_ascending))
        self.assertFalse(is_empty(self.list_same_size))
        self.assertFalse(is_empty(self.tuple_neg_taxi))
        self.assertFalse(is_empty(self.tuple_even))
        self.assertFalse(is_empty(self.tuple_non_unique))
        self.assertFalse(is_empty(self.tuple_list))
        
    def test_length(self):
        self.assertEqual(length(None), -1)
        self.assertEqual(length(self.list_empty), 0)
        self.assertEqual(length(self.list_taxi), 4)
        self.assertEqual(length(self.list_neg_pos), 5)
        self.assertEqual(length(self.list_descending), 6)
        self.assertEqual(length(self.list_ascending), 6)
        self.assertEqual(length(self.list_same_size), 4)
        self.assertEqual(length(self.tuple_neg_taxi), 4)
        self.assertEqual(length(self.tuple_even), 6)
        self.assertEqual(length(self.tuple_non_unique), 7)
        self.assertEqual(length(self.tuple_list), 9)
        
    def test_first_item(self):
        self.assertEqual(first_item(None), None)
        self.assertEqual(first_item(self.list_empty), None)
        self.assertEqual(first_item(self.list_taxi), 10)
        self.assertEqual(first_item(self.list_neg_pos), 10)
        self.assertEqual(first_item(self.list_descending), 9)
        self.assertEqual(first_item(self.list_ascending), -17)
        self.assertEqual(first_item(self.list_same_size), [10, 70, 20, 90])
        self.assertEqual(first_item(self.tuple_neg_taxi), -10)
        self.assertEqual(first_item(self.tuple_even), 4)
        self.assertEqual(first_item(self.tuple_non_unique), 4)
        self.assertEqual(first_item(self.tuple_list), [])
    
    
    def test_sum(self):
        self.assertEqual(sum(None), -1)
        self.assertEqual(sum(self.list_empty), 0)
        self.assertEqual(sum(self.list_taxi), 190)
        self.assertEqual(sum(self.list_neg_pos), 32)
        self.assertEqual(sum(self.list_descending), -6)
        self.assertEqual(sum(self.list_ascending), -6)
        self.assertEqual(sum(self.tuple_neg_taxi), -190)
        self.assertEqual(sum(self.tuple_even), 144)
        self.assertEqual(sum(self.tuple_non_unique), 233)
     
    
    def test_count_even(self):
        self.assertEqual(count_even(None), -1)
        self.assertEqual(count_even(self.list_empty), 0)
        self.assertEqual(count_even(self.list_taxi), 190)
        self.assertEqual(count_even(self.list_neg_pos), 16)
        self.assertEqual(count_even(self.list_descending), 4)
        self.assertEqual(count_even(self.list_ascending), 4)
        self.assertEqual(count_even(self.tuple_neg_taxi), -190)
        self.assertEqual(count_even(self.tuple_even), 144)
        self.assertEqual(count_even(self.tuple_non_unique), 228)
      
    
    def test_find_min(self):
        self.assertEqual(find_min(None), None)
        self.assertEqual(find_min(self.list_empty), None)
        self.assertEqual(find_min(self.list_taxi), 10)
        self.assertEqual(find_min(self.list_neg_pos), -8)
        self.assertEqual(find_min(self.list_descending), -17)
        self.assertEqual(find_min(self.list_ascending), -17)
        self.assertEqual(find_min(self.tuple_neg_taxi), -90)
        self.assertEqual(find_min(self.tuple_even), -2)
        self.assertEqual(find_min(self.tuple_non_unique), 4)
        
    def test_find_min_max(self):
        self.assertEqual(find_min_max(None), None)
        self.assertEqual(find_min_max(self.list_empty), None)
        self.assertEqual(find_min_max(self.list_taxi), (10, 90))
        self.assertEqual(find_min_max(self.list_neg_pos), (-8, 21))
        self.assertEqual(find_min_max(self.list_descending), (-17, 9))
        self.assertEqual(find_min_max(self.list_ascending), (-17, 9))
        self.assertEqual(find_min_max(self.tuple_neg_taxi), (-90, -10))
        self.assertEqual(find_min_max(self.tuple_even), (-2, 100))
        self.assertEqual(find_min_max(self.tuple_non_unique), (4, 70))
     
    
    def test_all_positive(self):
        self.assertFalse(all_positive(None))
        self.assertTrue(all_positive(self.list_empty))
        self.assertTrue(all_positive(self.list_taxi))
        self.assertFalse(all_positive(self.list_neg_pos))
        self.assertFalse(all_positive(self.list_descending))
        self.assertFalse(all_positive(self.list_ascending))
        self.assertFalse(all_positive(self.tuple_neg_taxi))
        self.assertFalse(all_positive(self.tuple_even))
        self.assertTrue(all_positive(self.tuple_non_unique))
        
    def test_atleast_one_divisible(self):
        self.assertFalse(atleast_one_divisible(None, 5))
        self.assertFalse(atleast_one_divisible(self.list_empty, 5))
        self.assertTrue(atleast_one_divisible(self.list_taxi, 1))
        self.assertTrue(atleast_one_divisible(self.list_taxi, 35))
        
        self.assertTrue(atleast_one_divisible(self.list_neg_pos, -4))
        self.assertFalse(atleast_one_divisible(self.tuple_even, 3))
        self.assertTrue(atleast_one_divisible(self.tuple_even, 7))
    
    def test_sum_even(self):
        self.assertEqual(sum_even(None), None)
        self.assertEqual(sum_even(self.list_empty), 0)
        self.assertEqual(sum_even(self.list_taxi), 190)
        self.assertEqual(sum_even(self.list_neg_pos), 16)
        self.assertEqual(sum_even(self.list_descending), 4)
        self.assertEqual(sum_even(self.list_ascending), 4)
        self.assertEqual(sum_even(self.tuple_neg_taxi), -190)
        self.assertEqual(sum_even(self.tuple_even), 144)
        self.assertEqual(sum_even(self.tuple_non_unique), 228)
    
    def test_add_even(self):
        self.assertEqual(add_even(None), [])
        self.assertEqual(add_even(self.list_empty), [])
        self.assertEqual(add_even(self.list_taxi), [10, 70, 20, 90])
        self.assertEqual(add_even(self.list_neg_pos), [10, 14, -8])
        self.assertEqual(add_even(self.list_descending), [8, -4])
        self.assertEqual(add_even(self.list_ascending), [-4, 8])
        self.assertEqual(add_even(self.tuple_neg_taxi), [-10, -70, -20, -90])
        self.assertEqual(add_even(self.tuple_even), [4, -2, 8, 20, 14, 100])
        self.assertEqual(add_even(self.tuple_non_unique), [4, 10, 70, 4, 70, 70])
    
    def test_power_indices(self):
        self.assertEqual(power_indices(None, 0, 2), None)
        self.assertEqual(power_indices(self.list_empty, 0, 1), [])
        self.assertEqual(power_indices(self.list_taxi, 1, 3), [10, 4900, 400, 90])
        self.assertEqual(self.list_taxi, [10, 4900, 400, 90])
        self.assertEqual(power_indices(self.list_taxi, 1, 10), [10, 24010000, 160000, 8100])
        self.assertEqual(power_indices(self.list_neg_pos, -2, 3), [100, 25, 196, -8, 21])
        self.assertEqual(power_indices(self.list_neg_pos, -2, 5), [10000, 625, 38416, 64, 441])
        
    def test_power_indices_2(self):
        self.assertEqual(power_indices_2(None, 0, 2), None)
        self.assertEqual(power_indices_2(self.list_empty, 0, 1), [])
        self.assertEqual(power_indices_2(self.list_taxi, 1, 3), [10, 4900, 400, 90])
        self.assertEqual(self.list_taxi, [10, 70, 20, 90])
        self.assertEqual(power_indices_2(self.list_taxi, 1, 10), [10, 4900, 400, 8100])
        self.assertEqual(power_indices_2(self.list_neg_pos, -2, 3), [100, 25, 196, -8, 21])
        self.assertEqual(power_indices_2(self.list_neg_pos, -2, 5), [100, 25, 196, 64, 441])
    
    
    def test_is_descending(self):
        self.assertFalse(is_descending(None))
        self.assertTrue(is_descending(self.list_empty))
        self.assertFalse(is_descending(self.list_taxi))
        self.assertFalse(is_descending(self.list_neg_pos))
        self.assertTrue(is_descending(self.list_descending))
        self.assertFalse(is_descending(self.list_ascending))
        self.assertFalse(is_descending(self.tuple_neg_taxi))
        self.assertFalse(is_descending(self.tuple_even))
        self.assertFalse(is_descending(self.tuple_non_unique))
        self.assertFalse(is_descending([10, 20, 20, 70, 90])) #not strictly descending
      
    
    def test_mutually_reverse(self):
        self.assertFalse(mutually_reverse(None, self.list_taxi))
        self.assertFalse(mutually_reverse(self.list_taxi, None))
        self.assertFalse(mutually_reverse(self.list_taxi, self.list_taxi))
        self.assertFalse(mutually_reverse(self.tuple_neg_taxi, self.list_taxi))
        self.assertTrue(mutually_reverse([90, 20, 70, 10], self.list_taxi))
        self.assertTrue(mutually_reverse((90, 20, 70, 10), self.list_taxi))
        self.assertTrue(mutually_reverse((70, 70, 5, 4, 70, 10, 4), self.tuple_non_unique))
    
    def test_all_unique(self):
        self.assertFalse(all_unique(None))
        self.assertTrue(all_unique(self.list_empty))
        self.assertTrue(all_unique(self.list_taxi))
        self.assertTrue(all_unique(self.list_neg_pos))
        self.assertTrue(all_unique(self.list_descending))
        self.assertTrue(all_unique(self.list_ascending))
        self.assertTrue(all_unique(self.tuple_neg_taxi))
        self.assertTrue(all_unique(self.tuple_even))
        self.assertFalse(all_unique(self.tuple_non_unique))
    
    
    def test_all_sublists_same_length(self):
        self.assertFalse(all_sublists_same_length(None))
        self.assertTrue(all_sublists_same_length(self.list_same_size))
        self.assertTrue(all_sublists_same_length([(1, 2), (4, 3), (20, 11)]))
        self.assertFalse(all_sublists_same_length(self.tuple_list))
        
    def test_sum_sublists(self):
        self.assertEqual(sum_sublists(None), [])
        self.assertEqual(sum_sublists(self.list_same_size), [190, -190, -5, 167])
        self.assertEqual(sum_sublists([(1, 2), (4, 3), (-20, 11)]), [3, 7, -9])
        self.assertEqual(sum_sublists(self.tuple_list), [0, 0, 190, 36, 0, 42, 370, 0, 167])
        
    def test_all_descending(self):
        self.assertFalse(all_descending(None))
        self.assertFalse(all_descending(self.list_same_size))
        self.assertFalse(all_descending(self.tuple_list))
        self.assertTrue(all_descending([(10, 7, 5), (3, 2, 1)]))
        self.assertFalse(all_descending([[10, 7, 6], [4], [5, 1]]))
        self.assertFalse(all_descending([[10, 7, 6], [4], [1, 1]]))
        self.assertFalse(all_descending([[10, 7, 6], [6], [5, 1]]))
     
        
if __name__ == "__main__":    
    unittest.main() 