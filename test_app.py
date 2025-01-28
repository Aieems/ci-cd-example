import unittest
from app import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEquals(sum(1,2), 3)


if __name__ == 'main':
    unittest.main()