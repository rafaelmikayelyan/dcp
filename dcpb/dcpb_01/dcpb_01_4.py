# Problem 1.4:
# Given an array of integers, return a new array where each element in the new array is the number
# of smaller elements to the right of that element in the original input array.

import unittest


def dcpb_01_4(array: list[int]) -> list[int]:
    smaller = []
    for i in range(0, len(array) - 1):
        counter = 0
        for j in range(i, len(array)):
            if array[i] > array[j]:
                counter += 1
        smaller.append(counter)
    smaller.append(0)

    return smaller


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(dcpb_01_4([3, 4, 9, 6, 1]), [1, 1, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
