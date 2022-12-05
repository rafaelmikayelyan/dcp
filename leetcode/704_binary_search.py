import unittest
import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            middle = left + (right - left) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
                
        return -1

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.search(self, [-1, 0, 3, 5, 9, 12], 9), 4)

    def test_2(self):
        self.assertEqual(Solution.search(self, [-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == '__main__':
    unittest.main()
