from cmath import log
from distutils.log import Log
from gettext import find
from random import random
import unittest
import math

def sum(n):
    """
    Return the sum of all integers in the range [1, n]
    """
    None

def count_divisible_by(n, start, end):
    """
    Count the numbers that are divisible by n in the range [start, end]. 
    Assume start <= end
    """
    None

def sum_even(start, end):
    """
    Return the sum of all even numbers in the range [start, end).
    Assume start < end and start is positive
    Challenge: solve it without using any if statement
    """
    None

def sum_even_2(n):
    """
    Return the sum of the first n positive EVEN integers (2+4+...+(2*n))
    """
    sum = 0
    for i in range(2, 2*n + 1, 2):
        sum = sum + i
    return sum

de
    None

de
    None

def is_prime(n):
    None

def num_primes(start, end):
    """
    Return the number of primes in the range (start, end)
    Assume start < end and start is non-negative
    """
    None

def binary(n):
    """
    Convert the positive number n to binary (base 2).
    Do not use the bin() function
    """
    None

def first_power(val, n):
    """
    return the first power of n that is
    not smaller than val. Do NOT use the
    built in pow() functions.
    
    For example: 
    val = 124, n = 5 -> since 5^3 = 125 return 125
    """
    None

def palindrome(str):
    """
    Return true is str is a palindrome and false otherwise.
    A palindrome is String that reads the same backwards and forwards.
    """
    None

def pyramids(n):
    """
    ADVANCED
    Based on https://open.kattis.com/problems/pyramids
    The number of bricks to build a pyramid of the following heights are:
        1: 1
        2: 10
        3: 35
        4: 84
    Given n blocks, what is the highest pyramid that can be built?
    """
    None

def scrambled_letters(str):
    """
    ADVANCED
    Given that the length of the input String is n, it will 
    contain n-1 of the first n lowercase letters of the 
    alphabet and 'z'.
    
    Every letter represents an index (a=0, b=1, c=2, ..) 
    that you should jump to. Given that you start at the 
    first letter in the String, how many jumps are needed to 
    reach 'z'?
    
    For example
        n = 3: 'bcz' will jump b -> c -> z. Answer 2
        n = 5: 'czecb' will jump c -> e -> b -> j. Answer 3
        
    Assume that the input will always have a valid solution.
    ord() function may be helpful.
    """
    None

def sum_multiple_even(start, end):
    """
    Sum the numbers in the range (start, end].
    But for every even number, add the sum of all
    later odd numbers (in the range) to the total sum.
    
    For example:
    start = 3, end = 8 -> sum = 3 + 4 + (5 + 7) + 5 + 6 + (7) + 7 = 44
    """
    None

class Tester(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1), 1)
        self.assertEqual(sum(2), 3)
        self.assertEqual(sum(3), 6)
        self.assertEqual(sum(10), 55)
        self.assertEqual(sum(7), 28)
        self.assertEqual(sum(30), 465)
        
    def test_count_divisible_by(self):
        self.assertEqual(count_divisible_by(1, 4, 11), 8)
        self.assertEqual(count_divisible_by(3, 3, 3), 1)
        self.assertEqual(count_divisible_by(3, 2, 7), 2)
        self.assertEqual(count_divisible_by(5, 10, 23), 3)
        self.assertEqual(count_divisible_by(5, 11, 24), 2)
        self.assertEqual(count_divisible_by(5, -11, 24), 7)
    
    def test_sum_even(self):
        self.assertEqual(sum_even(2, 6), 6)
        self.assertEqual(sum_even(6, 14), 36)
        self.assertEqual(sum_even(10, 20), 70)
        self.assertEqual(sum_even(5, 14), 36)
        self.assertEqual(sum_even(6, 15), 50)
        self.assertEqual(sum_even(5, 15), 50)
     
    def test_sum_even_2(self):
        self.assertEqual(sum_even_2(2), 6)
        self.assertEqual(sum_even_2(5), 30)
        self.assertEqual(sum_even_2(3), 12)
        self.assertEqual(sum_even_2(8), 72)
        self.assertEqual(sum_even_2(6), 42)
        self.assertEqual(sum_even_2(45), 2070)
        
    def test_divisible_in_range(self):
        self.assertTrue(divisible_in_range(3, 3, 3))
        self.assertTrue(divisible_in_range(9, 2, 7))
        self.assertTrue(divisible_in_range(20, 10, 23))
        self.assertTrue(divisible_in_range(45, 10, 23))
        self.assertTrue(divisible_in_range(14, 0, 3))
        self.assertTrue(divisible_in_range(22, 11, 12))
        self.assertFalse(divisible_in_range(47, 10, 23))
        self.assertFalse(divisible_in_range(1, 4, 11))
        self.assertFalse(divisible_in_range(5, 11, 24))
        self.assertFalse(divisible_in_range(47, 0, 0))
        self.assertTrue(divisible_in_range(8, -3, 0))
        
    def test_is_prime(self):
        for i in range(1, 36):
            if i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19 or i == 23 or i == 29 or i == 31:
                self.assertTrue(is_prime(i))
            else:
                self.assertFalse(is_prime(i))
                
    def test_num_primes(self):
        self.assertEqual(num_primes(0, 8), 4)
        self.assertEqual(num_primes(1, 11), 4)
        self.assertEqual(num_primes(2, 11), 3)
        self.assertEqual(num_primes(2, 12), 4)
        self.assertEqual(num_primes(45, 256), 40)
        self.assertEqual(num_primes(17, 165), 31)
        self.assertEqual(num_primes(15, 165), 32)
        self.assertEqual(num_primes(17, 17), 0)
        self.assertEqual(num_primes(16, 17), 0)
        
    def test_binary(self):
        for i in range(1, 5000):
            self.assertEqual(binary(i), bin(i)[2:])
            
    def test_first_power(self):
        self.assertEqual(first_power(124, 5), 125)
        self.assertEqual(first_power(16, 2), 16)
        self.assertEqual(first_power(31, 2), 32)
        self.assertEqual(first_power(900, 3), 2187)
        self.assertEqual(first_power(900, -3), 6561)
        self.assertEqual(first_power(-3, -90), 8100)
        
    def test_palindrome(self):
        self.assertTrue(palindrome(""))
        self.assertTrue(palindrome("I"))
        self.assertTrue(palindrome("anna"))
        self.assertTrue(palindrome("level"))
        self.assertTrue(palindrome("kayak"))
        self.assertTrue(palindrome("redder"))
        self.assertFalse(palindrome("refers"))
        self.assertFalse(palindrome("Madam"))
        self.assertFalse(palindrome("madim"))
        self.assertFalse(palindrome("hanoah"))
        
    def test_pyramids(self):
        self.assertEqual(pyramids(1), 1)
        self.assertEqual(pyramids(10), 2)
        self.assertEqual(pyramids(35), 3)
        self.assertEqual(pyramids(84), 4)
        self.assertEqual(pyramids(85), 4)
        self.assertEqual(pyramids(83), 3)
        self.assertEqual(pyramids(70), 3)
        self.assertEqual(pyramids(95038230423), 4146)
        
    def test_scrambled_letters(self):
        self.assertEqual(scrambled_letters('bcz'), 2)
        self.assertEqual(scrambled_letters('czecb'), 3)
        self.assertEqual(scrambled_letters('zabcdef'), 0)
        self.assertEqual(scrambled_letters('hacacacz'), 1)
        self.assertEqual(scrambled_letters('bgzacae'), 4)
        
    def test_sum_multiple_even(self):
        self.assertEqual(sum_multiple_even(3, 8), 44)
        self.assertEqual(sum_multiple_even(2, 8), 61)
        self.assertEqual(sum_multiple_even(4, 9), 49)
        self.assertEqual(sum_multiple_even(5, 12), 114)
    
if __name__ == "__main__":    
    unittest.main() 