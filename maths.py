import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    
    @staticmethod
    def substraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)
    
    def test_substraction(self):
        result = SimpleMath.substraction(3, 2)
        self.assertEqual(result, 1)