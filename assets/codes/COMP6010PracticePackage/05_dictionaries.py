from cmath import log
from distutils.log import Log
from gettext import find
from random import random
import unittest
import math

def is_none(data):
    """
    Return true if data is None, false otherwise.
    """
    None

def add_value(data, key, value):
    """
    If the key doesn't yet exist, add the 
    key and value pair to the dictionary.
    """
    None

def occurances(data):
    """
    Given the list/tuple data, create a dictionary containing
    the number of occurances of every item in the list/tuple.
    If data is ivalid, return None
    """
    None

def min_dist(data):
    """
    Given a list of data, find the minimum distance between
    two identical items in the list. If no identical items exists,
    the minimum distance is the length of the list.
    If data is ivalid, return None
    
    Use only one loop to solve this problem.
    """
    None

def most_popular_list(data):
    """
    Given a list of lists as the input, find the most popular
    sublist. Return the sorted sublist(s) and the number of occurances
    in data.
    If data is ivalid, return None
    
    If there is more than 1 most popular sublist, they should all be returned.
    """
    None

class Tester(unittest.TestCase):
    def test_is_none(self):
        self.assertTrue(is_none(None))
        self.assertFalse(is_none({10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"}))
        
    def test_add_value(self):
        self.assertEqual(add_value(None, 0, 5), {0:5})
        self.assertEqual(add_value({10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"}, 10, "Afroja"), {10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"})
        self.assertEqual(add_value({10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan"}, "Nat", "David"), {10:"Gaurav", 70:"Carl", 20:"Emilie", 90:"Yan", "Nat":"David"})
        
    def test_occurances(self):
        self.assertEqual(occurances(None), None)
        self.assertEqual(occurances([10, 70, 20, 90]), {10:1, 70:1, 20:1, 90:1})
        self.assertEqual(occurances([10, 70, 20, 20, 20, 90, "Nat", 70, 10, "Charanya"]), {10:2, 70:2, 20:3, 90:1, "Nat":1, "Charanya":1})
        
    def test_min_dist(self):
        self.assertEqual(min_dist(None), None)
        self.assertEqual(min_dist([10, 70, 20, 90]), 4)
        self.assertEqual(min_dist([10, 70, 20, 20, 20, 90, "Nat", 70, 10, "Charanya"]), 1)
        self.assertEqual(min_dist([70, 20, 10, "Gaurav", 90, 70, 10, "Gaurav"]), 4)
        self.assertEqual(min_dist([10, 70, 20, 10, 20, 90, "Nat", 70, 10, "Charanya"]), 2)
        
    def test_most_popular_list(self):
        self.assertEqual(most_popular_list(None), None)
        self.assertEqual(
            most_popular_list([[10, 70, 20, 90], 
                               [10, 70, 20, 90], 
                               [10, 90, 20, 70]]), ([(10, 20, 70, 90)], 3))
        self.assertEqual(
            most_popular_list([[10, 70, 20, 90], 
                               [1, 7, 20, 90], 
                               [10, 90, 20, 70],
                               [1, 20, 7, 90],
                               [90, 7, 20, 1]]), ([(1, 7, 20, 90)], 3))
        self.assertEqual(
            most_popular_list([[10, 70, 20, 90], 
                               [-1, 7, 20, 90], 
                               [10, 90, 20, 70],
                               [-1, 90, 7, 20], 
                               [-1, -7, 4, 33]]), ([(10, 20, 70, 90), (-1, 7, 20, 90)], 2))
        
if __name__ == "__main__":    
    unittest.main() 