# Problem 1.2: given an array of int that are out of order,
# determine the bounds of the smallest window that must
# be sorted in order for the entire arr to be sorted.

import unittest


def dcpb012(array):
    pass


class Test(unittest.TestCase):
    def test_array_of_5(self):
        self.assertEqual(dcpb012([3, 7, 5, 6, 9]), (1, 3), "should be (1, 3)")


if __name__ == '__main__':
    unittest.main()
