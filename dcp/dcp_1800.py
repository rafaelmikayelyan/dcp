# DCP 1800
#
# Write a program that checks whether an integer is a palindrome.
# For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
# Do not convert the integer into a string.


import unittest


def dcp1800(number):
    if number < 10:
        return True
    if number % 10 == 0:
        return False
    reverse = 0
    temp = number
    while temp != 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    return reverse == number


class Test(unittest.TestCase):
    def test_0(self):
        self.assertTrue(dcp1800(0), "")

    def test_121(self):
        self.assertTrue(dcp1800(121), "")

    def test_888(self):
        self.assertTrue(dcp1800(888), "")

    def test_826628(self):
        self.assertTrue(dcp1800(826628), "")

    def test_12(self):
        self.assertFalse(dcp1800(12), "")

    def test_678(self):
        self.assertFalse(dcp1800(678), "")

    def test_288992(self):
        self.assertFalse(dcp1800(288992), "")

    def test_2220(self):
        self.assertFalse(dcp1800(2220), "")


if __name__ == '__main__':
    unittest.main()
