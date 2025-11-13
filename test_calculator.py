import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        

   
    # Add the following test methods to the TestCalculator class:
        
    # Add
    def test_add2(self):
        self.assertEqual(self.calc.add(5, 5), 10)
    def test_add2(self):
        self.assertEqual(self.calc.add(-4, -6), -10)

    # SUBTRACT
    def test_sub1(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # Multiply
    def test_mul1(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(-5, 5), -25)

    # Divide
    def test_divide1(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(12, 5), 2)
    # Modulus
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(99, 10), 9)

if __name__ == '__main__':
    unittest.main()