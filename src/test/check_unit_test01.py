#unittest
import unittest

class MyTest(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(1+1, 2)
    
    def test_subtraction(self):
        self.assertEqual(2-1, 1)

if __name__ == '__main__':
    unittest.main()