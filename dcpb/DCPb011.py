# Problem 1.1: given an arr of int, return a new
# arr such that each element at i of the new arr
# is the product of all the num in the original
# arr except the one at i.
# Extra: no division.

import unittest


def dcpb011(array):
    if check_array_is_valid(array):
        return divide_product(array, array_product(array))
    else:
        return False


def array_product(array):
    product = 1
    i = 0
    while i < len(array):
        product = product * array[i]
        i += 1
    return product


def divide_product(array, product):
    i = 0
    while i < len(array):
        # '/' returns float, '//' returns integer
        array[i] = product // array[i]
        i += 1
    return array


def dcpb011_extra(array):
    return False


def check_array_is_valid(array):
    if check_array_length(array) or check_array_int(array):
        return False
    return True


def check_array_length(array):
    if not (hasattr(array, "__len__")):
        return True
    if len(array) < 2:
        return True


def check_array_int(array):
    for i in array:
        if not isinstance(i, int):
            return True


class Test(unittest.TestCase):
    def test_array_wrong_input_str(self):
        self.assertFalse(dcpb011("x"), "should be an array of #'s size=2+")

    def test_array_wrong_input_int(self):
        self.assertFalse(dcpb011(1), "should be an array of #'s size=2+")

    def test_array_with_string(self):
        self.assertFalse(dcpb011([1, "x"]), "should be an array of #'s size=2+")

    def test_array_of_0(self):
        self.assertFalse(dcpb011([]), "should be an array of #'s size=2+")

    def test_array_of_1(self):
        self.assertFalse(dcpb011([3]), "should be an array of #'s size=2+")

    def test_array_of_2(self):
        self.assertEqual(dcpb011([1, 2]), [2, 1], "should be [2, 1]")

    def test_array_of_3(self):
        self.assertEqual(dcpb011([2, 3, 4]), [12, 8, 6], "should be [12, 8, 6]")

    def test_array_of_5(self):
        self.assertEqual(dcpb011([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24], "should be [120, 60, 40, 30, 24]")

    def test_extra_array_wrong_input_str(self):
        self.assertFalse(dcpb011_extra("x"), "should be an array of #'s size=2+")

    def test_extra_array_wrong_input_int(self):
        self.assertFalse(dcpb011_extra(1), "should be an array of #'s size=2+")

    def test_extra_array_with_string(self):
        self.assertFalse(dcpb011_extra([1, "x"]), "should be an array of #'s size=2+")

    def test_extra_array_of_0(self):
        self.assertFalse(dcpb011_extra([]), "should be an array of #'s size=2+")

    def test_extra_array_of_1(self):
        self.assertFalse(dcpb011_extra([3]), "should be an array of #'s size=2+")

    def test_extra_array_of_2(self):
        self.assertEqual(dcpb011_extra([1, 2]), [2, 1], "should be [2, 1]")

    def test_extra_array_of_3(self):
        self.assertEqual(dcpb011_extra([2, 3, 4]), [12, 8, 6], "should be [12, 8, 6]")

    def test_extra_array_of_5(self):
        self.assertEqual(dcpb011_extra([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24], "should be [120, 60, 40, 30, 24]")

if __name__ == '__main__':
    unittest.main()
