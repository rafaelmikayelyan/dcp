# Problem 1.3: given an ar of num, find
# the max sum of any contiguous subarr of the arr.
# Do in O(n)
# Extra: what if elements can wrap around (last + first)

import unittest


def dcpb013(array):
    max_sum = 0
    for i in range(len(array) - 1):
        for j in range(i, len(array) + 1):
            max_sum = max(max_sum, sum(array[i:j]))
    return max_sum


class Test(unittest.TestCase):
    def test_array_sum_137(self):
        self.assertEqual(dcpb013([34, -50, 42, 14, -5, 86]), 137,
                         "137 from [42, 14, -5, 86]")

    def test_array_sum_0(self):
        self.assertEqual(dcpb013([-34, -50, -42, -14, -5, -86]), 0,
                         "0 from []")

    # def test_extra_array(self):
    #     self.assertEqual(dcpb013_extra([8, -1, 3, 4]), 15,
    #                      "15 from [3, 4, 8]")


if __name__ == '__main__':
    unittest.main()
