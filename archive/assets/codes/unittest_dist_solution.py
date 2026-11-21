from cmath import sqrt
import unittest

class Tester(unittest.TestCase):
    def test_dist(self):
        self.assertAlmostEqual(dist(0,0,0,0), 0)
        self.assertAlmostEqual(dist(1,1,0,0), sqrt(2))
        self.assertAlmostEqual(dist(1,2,3,4), sqrt(8), 2)
        self.assertAlmostEqual(dist(1,7,2,9), 2.236, 3)
    
'''
return distance between points (x1, y1) and (x2, y2)
'''
def dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    distSquare = dx*dx + dy*dy
    return sqrt(distSquare)

if __name__ == "__main__":    
    unittest.main() 
