from cmath import log
from distutils.log import Log
from gettext import find
from random import random
import unittest
import math

def get_last_digit(n):
    """
    Return the last digit assuming that n is non-negative
    """
    None

def get_negative_last_digit(n):
    """
    Return the last digit assuming that n is negative
    """
    None

def get_second_last_digit(n):
    None

def get_first_digit(n):
    None

def both_even(a, b):
    None

def both_odd(a, b):
    None

def different_oddity(a, b):
    None

def atleast_one_odd(a, b, c, d, e):
    None

def higher(a, b, c):
    """
    Return the highest value
    """
    None

def first_char(str):
    None

def last_char(str):
    None

def all_but_first_word(str):
    """
    assume there are at least two words in the string,
    and each word is separated by a single space.
    there are no leading or trailing spaces in the string.
    """
    None

def caesar_cipher(letter, n):
    """
    Given a lower case letter, shift it n spots forward in 
    the english alphabet. Assume n is always positive.
    Hint: The chr() and ord() fuctions can be helpful
    """
    None

def manhattan_distance(ax, ay, bx, by):
    """
    Find the manhattan distance between the two points a and b.
    Manhattan distance is the sum of the absolute difference between
    two points.
    """
    None

def distance(ax, ay, bx, by):
    """
    Return the distance between the two points a and b.
    Pythagoras theorem may be helpful
    """
    None

def decimal_difference(n):
    """
    Return how much n has to change to become a whole number.
    """
    None

def days_in_year(year):
    None

def find_substring(str, start, end):
    """
    Return the String between [start, end).
    If either start or end is invalid, return None.
    Note: () - declusive brackets.
          [] - inclusive brackets.
    """
    None

def compare_to(a, b):
    """
    Return 1 if a is more than b.
          -1 if a is less than b.
           0 if they have the same value
    """
    None

def next_multiple(val, n):
    """
    Given the value val, find the smallest multiple of n
    that is higher than val.
    Assume n and val are positive.
    """
    None

def reverse(str):
    """
    Return the reverse of str
    """
    None

def generate_randomized_total():
    """
    should return a total between 0 and 10000 with at randomized 2 digits of precision
    """
    None

class Tester(unittest.TestCase):
            
    def test_get_last_digit(self):
        self.assertEqual(get_last_digit(1729), 9)
        self.assertEqual(get_last_digit(23528435), 5)
        self.assertEqual(get_last_digit(235284), 4)
        self.assertEqual(get_last_digit(3), 3)
    
    def test_get_negative_last_digit(self):
        self.assertEqual(get_negative_last_digit(-1729), 9)
        self.assertEqual(get_negative_last_digit(-23528435), 5)
        self.assertEqual(get_negative_last_digit(-235284), 4)
        self.assertEqual(get_negative_last_digit(-3), 3)

    def test_get_second_last_digit(self):
        self.assertEqual(get_second_last_digit(1729), 2)
        self.assertEqual(get_second_last_digit(23528435), 3)
        self.assertEqual(get_second_last_digit(16), 1)
        self.assertEqual(get_second_last_digit(-1729), 2)
        self.assertEqual(get_second_last_digit(-23528435), 3)
        self.assertEqual(get_second_last_digit(-16), 1)

    def test_get_first_digit(self):
        self.assertEqual(get_first_digit(1729), 1)
        self.assertEqual(get_first_digit(31729), 3)
        self.assertEqual(get_first_digit(2), 2)
        self.assertEqual(get_first_digit(-1729), 1)
        self.assertEqual(get_first_digit(-31729), 3)
        self.assertEqual(get_first_digit(-2), 2)

    def test_both_even(self):
        self.assertTrue(both_even(12, 18))
        self.assertTrue(both_even(-12, 18))
        self.assertTrue(both_even(12, 0))
        self.assertFalse(both_even(12, 17))
        self.assertFalse(both_even(17, 12))
        self.assertFalse(both_even(-19, 17))
        self.assertFalse(both_even(0, 17))

    def test_both_odd(self):
        self.assertTrue(both_odd(19, 17))
        self.assertTrue(both_odd(-19, 17))
        self.assertTrue(both_odd(19, -17))
        self.assertTrue(both_odd(1729, 927113))
        self.assertFalse(both_odd(12, 18))
        self.assertFalse(both_odd(-12, 18))
        self.assertFalse(both_odd(-12, 17))
        self.assertFalse(both_odd(12, 0))
        self.assertFalse(both_odd(12, 17))
        self.assertFalse(both_odd(17, 12))
        self.assertFalse(both_odd(0, 17))

    def test_different_oddity(self):
        self.assertFalse(different_oddity(19, 17))
        self.assertFalse(different_oddity(-19, 17))
        self.assertFalse(different_oddity(19, -17))
        self.assertFalse(different_oddity(1729, 927113))
        self.assertFalse(different_oddity(12, 18))
        self.assertFalse(different_oddity(-12, 18))
        self.assertTrue(different_oddity(-12, 17))
        self.assertFalse(different_oddity(12, 0))
        self.assertTrue(different_oddity(12, 17))
        self.assertTrue(different_oddity(17, 12))
        self.assertTrue(different_oddity(0, 17))

    def test_atleast_one_odd(self):
        self.assertFalse(atleast_one_odd(10, 20, 30, 40, 50))
        self.assertTrue(atleast_one_odd(11, 20, 30, 40, 50))
        self.assertTrue(atleast_one_odd(-11, 20, 30, 40, 50))
        self.assertTrue(atleast_one_odd(10, 27, 30, 40, 50))
        self.assertTrue(atleast_one_odd(10, -27, 30, 40, 50))
        self.assertTrue(atleast_one_odd(10, 20, 31, 40, 50))
        self.assertTrue(atleast_one_odd(10, 20, -31, 40, 50))
        self.assertTrue(atleast_one_odd(10, 20, 30, 45, 50))
        self.assertTrue(atleast_one_odd(10, 20, 30, -45, 50))
        self.assertTrue(atleast_one_odd(10, 20, 30, 40, 59))
        self.assertTrue(atleast_one_odd(10, 20, 30, 40, -59))
        self.assertTrue(atleast_one_odd(19, 20, 31, 40, 50))
        self.assertTrue(atleast_one_odd(10, 21, 30, 47, 53))
        self.assertTrue(atleast_one_odd(11, 23, 35, 47, 50))
        self.assertTrue(atleast_one_odd(10, 29, 37, 45, 53))
        
            
    def test_higher(self):
        self.assertEqual(higher(10, 70, 20), 70)
        self.assertEqual(higher(70, 10, 20), 70)
        self.assertEqual(higher(10, 20, 70), 70)
        self.assertEqual(higher(10, 20, 20), 20)
        self.assertEqual(higher(20, 10, 20), 20)
        self.assertEqual(higher(20, 20, 20), 20)
        self.assertEqual(higher(1, 11, 2.5), 11)
        
    def test_first_char(self):
        self.assertEqual(first_char("Super Nintendo Chalmers"), 'S')
        self.assertEqual(first_char("Nintendo"), 'N')
        self.assertEqual(first_char("$"), '$')
        
    def test_last_char(self):
        self.assertEqual(last_char("Super Nintendo Chalmers!"), '!')
        self.assertEqual(last_char("Nintendo"), 'o')
        self.assertEqual(last_char("$"), '$')
        
    def test_all_but_first_word(self):
        self.assertEqual(all_but_first_word("Super Nintendo Chalmers"), "Nintendo Chalmers")
        self.assertEqual(all_but_first_word("There's literally no one in the world that I don't hate right now"), "literally no one in the world that I don't hate right now")
        self.assertEqual(all_but_first_word("I am removing the first word"), "am removing the first word")
        
    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher('a', 1), 'b')
        self.assertEqual(caesar_cipher('c', 3), 'f')
        self.assertEqual(caesar_cipher('z', 1), 'a')
        self.assertEqual(caesar_cipher('b', 26), 'b')
        self.assertEqual(caesar_cipher('k', 32), 'q')
        self.assertEqual(caesar_cipher('x', 85), 'e')
        self.assertEqual(caesar_cipher('p', 1065), 'o')
        
    def test_manhattan_distance(self):
        self.assertEqual(manhattan_distance(5, 1, 5, 4), 3)
        self.assertEqual(manhattan_distance(5, 4, 5, 1), 3)
        self.assertEqual(manhattan_distance(10, 1, 70, 1), 60)
        self.assertEqual(manhattan_distance(-10, 1, -70, 1), 60)
        self.assertEqual(manhattan_distance(10, 2, 70, 3), 61)
        self.assertEqual(manhattan_distance(10, 5, 90, 3), 82)
        
    def test_distance(self):
        self.assertAlmostEqual(distance(1, 5, 1, 5), 0, places=4)
        self.assertAlmostEqual(distance(5, 1, 5, 4), 3, places=4)
        self.assertAlmostEqual(distance(1, 3, 4, 5), 3.60555, places=4)
        self.assertAlmostEqual(distance(5, 4, 5, 1), 3, places=4)
        self.assertAlmostEqual(distance(34, 15, 2, 18), 32.1403, places=4)
        self.assertAlmostEqual(distance(-10, 1, -70, 1), 60, places=4)
        self.assertAlmostEqual(distance(10, 2, 70, 3), 60.008332, places=4)
        self.assertAlmostEqual(distance(10, 5, 90, 3), 80.02499, places=4)
        
    def test_decimal_difference(self):
        self.assertAlmostEqual(decimal_difference(10.0), 0, places=4)
        self.assertAlmostEqual(decimal_difference(70.5), 0.5, places=4)
        self.assertAlmostEqual(decimal_difference(20.25), 0.25, places=4)
        self.assertAlmostEqual(decimal_difference(90.75), 0.25, places=4)
        self.assertAlmostEqual(decimal_difference(-10.0), 0, places=4)
        self.assertAlmostEqual(decimal_difference(-70.5), 0.5, places=4)
        self.assertAlmostEqual(decimal_difference(-20.25), 0.25, places=4)
        self.assertAlmostEqual(decimal_difference(-90.75), 0.25, places=4)
        self.assertAlmostEqual(decimal_difference(20.504), 0.496, places=4)
        
    def test_days_in_year(self):
        self.assertAlmostEqual(days_in_year(2022), 365)
        self.assertAlmostEqual(days_in_year(2021), 365)
        self.assertAlmostEqual(days_in_year(2019), 365)
        self.assertAlmostEqual(days_in_year(2018), 365)
        self.assertAlmostEqual(days_in_year(2017), 365)
        self.assertAlmostEqual(days_in_year(2020), 366)
        self.assertAlmostEqual(days_in_year(2016), 366)
        self.assertAlmostEqual(days_in_year(2000), 366)
        self.assertAlmostEqual(days_in_year(2800), 366)
        self.assertAlmostEqual(days_in_year(1900), 365)
        self.assertAlmostEqual(days_in_year(1800), 365)
        
    def test_next_multiple(self):
        self.assertEqual(next_multiple(12, 5), 15)
        self.assertEqual(next_multiple(10, 5), 15)
        self.assertEqual(next_multiple(23, 6), 24)
        self.assertEqual(next_multiple(14, 14), 28)
        self.assertEqual(next_multiple(14, 15), 15)
        
    def test_compare_to(self):
        self.assertEqual(compare_to(10, 70), -1)
        self.assertEqual(compare_to(70, 10), 1)
        self.assertEqual(compare_to(90, 90), 0)
        
        self.assertEqual(compare_to(5.4, 4.3), 1)
        self.assertEqual(compare_to(4.3, 4.4), -1)
        self.assertEqual(compare_to(10.3, 10.3), 0)
        
        self.assertEqual(compare_to(True, False), 1)
        self.assertEqual(compare_to(False, True), -1)
        self.assertEqual(compare_to(True, True), 0)
        
        self.assertEqual(compare_to("Desk", "Desks"), -1)
        self.assertEqual(compare_to("a", "b"), -1)
        self.assertEqual(compare_to("b", "a"), 1)
        self.assertEqual(compare_to("Hello", "nintendo"), -1)
        self.assertEqual(compare_to("hello", "Nintendo"), 1)
        self.assertEqual(compare_to("Same", "Same"), 0)
        
    def test_find_substring(self):
        self.assertIsNone(find_substring("Hello", -1, 3))
        self.assertIsNone(find_substring("Hello", 2, 10))
        self.assertIsNone(find_substring("Hello", 3, 1))
        self.assertEqual(find_substring("Hello", 1, 3), "el")
        self.assertEqual(find_substring("Nintendo", 0, 4), "Nint")
        self.assertEqual(find_substring("Nintendo", 4, 8), "endo")
        
    def test_reverse(self):
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("abc"), "cba")
        self.assertEqual(reverse("super"), "repus")
    
    def test_generate_randomized_total(self):
        occurances = {}
        for i in range(50000):
            total = generate_randomized_total()
            dec = total - (int)(total)
            self.assertLessEqual(total, 10000)
            self.assertLessEqual(dec, 100)
            self.assertGreaterEqual(total, 0)
            
            occurances[total] = occurances.get(total, 0) + 1
            self.assertLessEqual(occurances[total], 10)
        

if __name__ == "__main__":    
    unittest.main() 

