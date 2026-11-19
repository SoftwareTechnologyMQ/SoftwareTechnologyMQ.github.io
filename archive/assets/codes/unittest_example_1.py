import unittest

class Tester(unittest.TestCase):
    def test_is_positive(self):
        self.assertTrue(is_positive(5635.5))
        self.assertTrue(is_positive(1))
        self.assertTrue(is_positive(0.1))
        self.assertTrue(is_positive(0.01))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-0.1))
        self.assertFalse(is_positive(-0.01))
        self.assertFalse(is_positive(-11454.4))
    
def is_positive(val):
    if val > 0:
        return True
    else:
        return False

if __name__ == "__main__":    
    unittest.main() 
