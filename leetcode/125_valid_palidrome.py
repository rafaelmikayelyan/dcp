import unittest


class Solution:
    def isPalidrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left != right and left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.isPalidrome(self, "A man, a plan, a canal: Panama"), True)

    def test_2(self):
        self.assertEqual(Solution.isPalidrome(self, "race a car"), False)

    def test_3(self):
        self.assertEqual(Solution.isPalidrome(self, " "), True)


if __name__ == '__main__':
    unittest.main()
