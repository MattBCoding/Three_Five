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

    def test_multiples_of_three_and_five(self):
        """Test that multiples of three and five print 'ThreeFive'"""
        self.assertEqual(three_five(15), "ThreeFive")
        self.assertEqual(three_five(30), "ThreeFive")
        self.assertEqual(three_five(45), "ThreeFive")
        self.assertEqual(three_five(60), "ThreeFive")
        self.assertEqual(three_five(75), "ThreeFive")

    def test_other_numbers(self):
        """Test other numbers print the number"""
        self.assertEqual(three_five(1), 1)
        self.assertEqual(three_five(2), 2)
        self.assertEqual(three_five(4), 4)
        self.assertEqual(three_five(7), 7)
        self.assertEqual(three_five(8), 8)
        self.assertEqual(three_five(11), 11)


if __name__ == "__main__":
    unittest.main()
