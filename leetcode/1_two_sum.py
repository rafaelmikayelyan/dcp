import unittest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.twoSum(self, [2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(Solution.twoSum(self, [3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(Solution.twoSum(self, [3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()
