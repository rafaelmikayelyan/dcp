# Problem 1.2: given an array of int that are out of order,
# determine the bounds of the smallest window that must
# be sorted in order for the entire arr to be sorted.

import unittest


def dcpb012(array):
    left = get_left(array)
    return left, get_right(array, left)


def get_left(array):
    left = i = 0
    while i < len(array):
        if array[i] < array[left]:
            return left
        left = i
        i += 1
    return i


def get_right(array, left):
    array_length = len(array) - 1
    right = array_length
    i = 0
    while i < len(array):
        if (array[array_length - i] > array[right]) or (array[left] > array[right]):
            return right
        i += 1
        right = (len(array) - i)
    return -1


class Test(unittest.TestCase):
    def test_array_of_8(self):
        self.assertEqual(dcpb012([3, 7, 5, 6, 9]), (1, 3), "should be (1, 3)")


if __name__ == '__main__':
    unittest.main()
