import unittest


def dcpb001(array):
    pass


class Test(unittest.TestCase):
    def test_array_wrong_input_str(self):
        self.assertFalse(dcpb001("x"), "should be an array of #'s size=2+")

    def test_array_wrong_input_int(self):
        self.assertFalse(dcpb001(1), "should be an array of #'s size=2+")

    def test_array_with_string(self):
        self.assertFalse(dcpb001([1, "x"]), "should be an array of #'s size=2+")

    def test_array_of_0(self):
        self.assertFalse(dcpb001([]), "should be an array of #'s size=2+")

    def test_array_of_1(self):
        self.assertFalse(dcpb001([3]), "should be an array of #'s size=2+")

    def test_array_of_2(self):
        self.assertEqual(dcpb001([1, 2]), [2, 1], "should be [2, 1]")

    def test_array_of_3(self):
        self.assertEqual(dcpb001([2, 3, 4]), [12, 8, 6], "should be [12, 8, 6]")

    def test_array_of_5(self):
        self.assertEqual(dcpb001([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24], "should be [120, 60, 40, 30, 24]")


if __name__ == '__main__':
    unittest.main()
