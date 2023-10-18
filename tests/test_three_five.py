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


if __name__ == "__main__":
    unittest.main()
