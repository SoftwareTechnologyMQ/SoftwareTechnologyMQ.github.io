from cmath import log
from distutils.log import Log
from gettext import find
from random import random
import unittest
import math

def cube(n):
    """
    Function name: cube()
    Define a function that when passed a number,
    returns the cube of that number.
    """
    None

def repeat_pattern(str, n):
    """
    Function name: repeat_pattern()
    Define a function that when passed a word,
    returns n occurances of that word.
    For example: "abc" repeated 3 times is "abcabcabc"
    """
    None

def mean(a, b, c):
    """
    Function name: mean()
    Define a function that returns the mean of 3 numbers
    """
    None

def median(a, b, c):
    """
    Function name: median()
    Define a function that returns the mean of 3 numbers
    """
    None

def num_digits(n):
    """
    Function name: num_digits()
    Define a function that when passed a number n,
    returns the number of digits in n.
    """
    None

def sum_digits(n):
    """
    Function name: sum_digits()
    Define a function that when passed a number,
    returns the sum of digits in that number.
    """
    None

def sum_digits_less(n, d):
    """
    Function name: sum_digits_less()
    Define a function that when passed a number,
    returns the sum of digits in n that are less then the
    second parameter d.
    """
    None

def gcd(a, b):
    """
    Function name: gcd()
    Define a function that returns the greatest
    common denominator between 2 positive numbers.
    """
    None

def sum_odd(start, end):
    """
    Function name: sum_odd()
    Define a function that returns the sum of all ODD numbers 
    in the range [start, end). 
    Assume start < end and start is positive
    """
    None

def sum_odd_2(n):
    """
    Function name: sum_odd_2()
    Define a function that returns the sum of the first n positive ODD integers
    """
    None

def contains_all(a, b):
    """
    Function name: contains_all()
    Define a function that returns true if the string a
    contains all the letters in string b
    
    For example: 
    all the letters in "lab" are also in "lambda"
    all the letters in "tea" are NOT in "nintendo"
    all the letters in "tee" are also in "nintendo" (the e can be used twice)
    """
    None

def remove_n(input, to_remove, n):
    """
    Function name: remove_n()
    Given an input String, a String to remove and a number n,
    remove the first n occurances of to_remove from the input.
    """
    None

class Tester(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(5), 125)
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(4), 64)
        self.assertEqual(cube(12), 1728)
        self.assertEqual(cube(-2), -8)
    
    def test_repeat_pattern(self):
        self.assertEqual(repeat_pattern("abc", 3), "abcabcabc")
        self.assertEqual(repeat_pattern("a", 4), "aaaa")
        self.assertEqual(repeat_pattern("hahi", 5), "hahihahihahihahihahi")
        
    def test_mean(self):
        self.assertEqual(mean(10, 15, 20), 15)
        self.assertEqual(mean(15, 10, 20), 15)
        self.assertEqual(mean(10, 20, 15), 15)
        self.assertAlmostEqual(mean(10, 10, 18), 12.6666, places=3)
        self.assertAlmostEqual(mean(11, 70, 14), 31.6666, places=3)
        self.assertAlmostEqual(mean(50, 20, 30), 33.3333, places=3)
        
    
    def test_median(self):
        self.assertEqual(median(10, 14, 20), 14)
        self.assertEqual(median(14, 10, 20), 14)
        self.assertEqual(median(10, 20, 14), 14)
        self.assertEqual(median(11, 70, 14), 14)
        self.assertEqual(median(50, 20, 30), 30)
        self.assertEqual(median(10, 10, 18), 10)
        self.assertEqual(median(10, 10, 10), 10)
        self.assertEqual(median(18, 10, 10), 10)
        self.assertEqual(median(10, 18, 10), 10)
    
    def test_num_digits(self):
        self.assertEqual(num_digits(1729), 4)
        self.assertEqual(num_digits(1729304), 7)
        self.assertEqual(num_digits(0), 0)
        self.assertEqual(num_digits(3), 1)
        self.assertEqual(num_digits(12643), 5)
    
    def test_sum_digits(self):
        self.assertEqual(sum_digits(1729), 19)
        self.assertEqual(sum_digits(1729304), 26)
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(3), 3)
        self.assertEqual(sum_digits(12643), 16)
    
    def test_sum_digit_less(self):
        self.assertEqual(sum_digits_less(1729, 8), 10)
        self.assertEqual(sum_digits_less(1729, 7), 3)
        self.assertEqual(sum_digits_less(17293504, 6), 15)
        self.assertEqual(sum_digits_less(34567, 2), 0)
    
    def test_gcd(self):
        self.assertEqual(gcd(100, 35), 5)
        self.assertEqual(gcd(35, 100), 5)
        self.assertEqual(gcd(15, 32), 1)
        self.assertEqual(gcd(-51, 153), 51)
        self.assertEqual(gcd(51, -153), 51)
        self.assertEqual(gcd(80, 36), 4)
    
    def test_sum_odd(self):
        self.assertEqual(sum_odd(3, 7), 8)
        self.assertEqual(sum_odd(-3, 7), 5)
        self.assertEqual(sum_odd(5, 8), 12)
        self.assertEqual(sum_odd(4, 7), 5)
        self.assertEqual(sum_odd(4, 8), 12)
        self.assertEqual(sum_odd(40, 93), 1716)
    
    def test_sum_odd_2(self):
        self.assertEqual(sum_odd_2(3), 9)
        self.assertEqual(sum_odd_2(7), 49)
        self.assertEqual(sum_odd_2(4), 16)
        self.assertEqual(sum_odd_2(9), 81)
        
    def test_contains_all(self):
        self.assertTrue(contains_all("lab", "lambda"))
        self.assertFalse(contains_all("tea", "nintendo"))
        self.assertTrue(contains_all("tee", "nintendo"))
        self.assertTrue(contains_all("abce", "bccade"))
        self.assertFalse(contains_all("abce", "ccade"))
        
    def test_remove_n(self):
        self.assertEqual(remove_n("nintendo", "n", 2), "itendo")
        self.assertEqual(remove_n("papaya", "pa", 10), "ya")
        self.assertEqual(remove_n("paApaya", "pa", 1), "Apaya")
        self.assertEqual(remove_n("A good cook could cook as many cookies as a good cook who could cook cookies", "coo", 4), "A good k could k as many kies as a good k who could cook cookies")
        self.assertEqual(remove_n("Silly Sally swiftly shooed seven silly sheep. The seven silly sheep Silly Sally shooed shilly-shallied south. These sheep shouldn't sleep in a shack.", "ill", 100), "Sy Sally swiftly shooed seven sy sheep. The seven sy sheep Sy Sally shooed shy-shallied south. These sheep shouldn't sleep in a shack.")
    
    
if __name__ == "__main__":    
    unittest.main() 