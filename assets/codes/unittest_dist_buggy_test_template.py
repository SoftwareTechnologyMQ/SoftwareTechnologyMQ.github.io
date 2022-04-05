from cmath import sqrt
import unittest

class Tester(unittest.TestCase):
    def test_dist(self):
        self.assertAlmostEqual(dist(0,0,0,0), 0)
        self.assertAlmostEqual(dist(1,1,0,0), sqrt(2))
        self.assertAlmostEqual(dist(1,2,3,4), 2.80, 2)
        self.assertAlmostEqual(dist(1,7,2,9), 2.336, 3)
    
'''
return distance between points (x1, y1) and (x2, y2)
'''
def dist(x1, y1, x2, y2):
    return 0

if __name__ == "__main__":    
    unittest.main() 
