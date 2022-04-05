import unittest

class Tester(unittest.TestCase):
    def test_is_in_range(self):
        self.assertTrue(is_in_range(10.2, 5.3, 18.9))
        self.assertTrue(is_in_range(-5.1, -5.1, 218.9))
        self.assertTrue(is_in_range(183.9, 5.3, 183.9))
        self.assertTrue(is_in_range(-5.09, -5.1, 218.9))
        self.assertTrue(is_in_range(183.8, 5.3, 183.9))
        self.assertFalse(is_in_range(5.2, 5.3, 18.9))
        self.assertFalse(is_in_range(18.91, 5.3, 18.9))
        self.assertFalse(is_in_range(-1118.9, 5.3, 1118.9))
        self.assertFalse(is_in_range(1729, 5.3, 1728))
        self.assertFalse(is_in_range(-5.11, -5.1, 218.9))
    
'''
return True if val is between low and high (inclusive on both sides), False otherwise.
'''
def is_in_range(val, low, high):
    if val >= low and val <= high:
        return True
    else:
        return False

if __name__ == "__main__":    
    unittest.main() 
