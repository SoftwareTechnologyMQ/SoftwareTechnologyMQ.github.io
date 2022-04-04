import unittest

class Tester(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(-5))
        self.assertTrue(is_odd(517))
        self.assertTrue(is_odd(-6561))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(8))
        self.assertFalse(is_odd(-8))
        self.assertFalse(is_odd(8096))
        self.assertFalse(is_odd(-8096))
    
def is_odd(val):
    if val%2 == 1:
        return True
    else:
        return False

if __name__ == "__main__":    
    unittest.main() 
