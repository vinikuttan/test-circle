import unittest
import time

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)
        
    def test_1(self):
        time.sleep(3)
        self.assertTrue(True)
        
    def test_2(self):
        time.sleep(3)
        self.assertTrue(True)   
        
    def test_3(self):
        time.sleep(3)
        self.assertTrue(True)
        
    def test_4(self):
        time.sleep(3)
        self.assertTrue(True)
        
    def test_5(self):
        time.sleep(3)
        self.assertTrue(True)
        
    def test_6(self):
        time.sleep(3)
        self.assertTrue(True)   
        

if __name__ == '__main__':
    unittest.main()
