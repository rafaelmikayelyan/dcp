import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in t:
            s = s.replace(i, '', 1)

        return len(s) == 0


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.isAnagram(self, "anagram", "nagaram"), True)

    def test_2(self):
        self.assertEqual(Solution.isAnagram(self, "rat", "car"), False)

    def test_3(self):
        self.assertEqual(Solution.isAnagram(self, "aacc", "ccac"), False)


if __name__ == '__main__':
    unittest.main()
