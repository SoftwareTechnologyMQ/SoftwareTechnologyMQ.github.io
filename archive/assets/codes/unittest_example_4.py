import unittest

class Tester(unittest.TestCase):
    def test_highest(self):
        self.assertEqual(3, highest(1, 1, 3))
        self.assertEqual(7, highest(5, 7, 5))
        self.assertEqual(-4, highest(-4, -10, -10))
        self.assertEqual(1, highest(1, 1, -3))
        self.assertEqual(5, highest(5, -7, 5))
        self.assertEqual(-10, highest(-14, -10, -10))
        self.assertEqual(1729, highest(1729, 1729, 1729))
        self.assertEqual(30, highest(10, 20, 30))
        self.assertEqual(100, highest(50, 100, 60))
        self.assertEqual(-100, highest(-500, -120, -100))
    
def highest(a, b, c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    else:
        if b>=c:
            return b
        else:
            return c

if __name__ == "__main__":    
    unittest.main() 
