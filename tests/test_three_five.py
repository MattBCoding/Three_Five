import unittest
from src.main import three_five


class TestThreeFive(unittest.TestCase):
    """A class to test the three_five function"""

    def test_multiples_of_three(self):
        """Test that multiples of three print 'Three'"""
        self.assertEqual(three_five(3), "Three")
        self.assertEqual(three_five(6), "Three")
        self.assertEqual(three_five(9), "Three")
        self.assertEqual(three_five(12), "Three")
        self.assertEqual(three_five(18), "Three")

    def test_multiples_of_five(self):
        """Test that multiples of five print 'Five'"""
        self.assertEqual(three_five(5), "Five")
        self.assertEqual(three_five(10), "Five")
        self.assertEqual(three_five(20), "Five")
        self.assertEqual(three_five(25), "Five")
        self.assertEqual(three_five(35), "Five")


if __name__ == "__main__":
    unittest.main()
