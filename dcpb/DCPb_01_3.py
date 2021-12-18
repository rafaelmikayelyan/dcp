# Problem 1.3: given an ar of num, find
# the max sum of any contiguous subarr of the arr.
# Do in O(n)
# Extra: what if elements can wrap around (last + first)

import unittest


def dcpb013(array):
    return False


class Test(unittest.TestCase):
    def test_array_sum(self):
        self.assertEqual(dcpb013([34, -50, 42, 14, -5, 86]), (137, [42, 14, -5, 86]),
                         "should be 137 from [42, 14, -5, 86]")

    # def test_extra_array(self):
    #     self.assertEqual(dcpb013_extra([8, -1, 3, 4]), (15, [3, 4, 8]),
    #                      "should be 137 from [42, 14, -5, 86]")


if __name__ == '__main__':
    unittest.main()
