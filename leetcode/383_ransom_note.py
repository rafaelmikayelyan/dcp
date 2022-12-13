import unittest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        skipIndex = []
        found = False

        for ransomIndex in range(0, len(ransomNote)):
            for magazineIndex in range(0, len(magazine)):
                if magazineIndex in skipIndex:
                    continue
                if ransomNote[ransomIndex] == magazine[magazineIndex]:
                    skipIndex.append(magazineIndex)
                    found = True
                    break

            if not found:
                break
            found = False

        return len(skipIndex) == len(ransomNote)


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.canConstruct(self, 'a', 'b'), False)

    def test_2(self):
        self.assertEqual(Solution.canConstruct(self, 'aa', 'ab'), False)

    def test_3(self):
        self.assertEqual(Solution.canConstruct(self, 'aa', 'aab'), True)

if __name__ == '__main__':
    unittest.main()
