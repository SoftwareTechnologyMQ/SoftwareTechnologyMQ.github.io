import unittest

class Tester(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(2.5, average(2, 3))
        self.assertAlmostEqual(-2.5, average(-2, -3))
        self.assertAlmostEqual(0, average(2, -2))
        self.assertAlmostEqual(-51.3, average(-51.1, -51.5))
    
def average(a, b):
    return (a+b)/2

if __name__ == "__main__":    
    unittest.main() 
