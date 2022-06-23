import unittest
import math


def solution(area):
    return best_sqrt(area, [])


def best_sqrt(remainder, nums=[]):
    if remainder == 0:
        return nums
    else: 
        last_num = remainder
        sqrt = math.sqrt(last_num)
        next_biggest = int(sqrt) ** 2
        nums.append(next_biggest)
        remainder = last_num - next_biggest
        return best_sqrt(remainder, nums)


class Test(unittest.TestCase):
    def test_12(self):
        self.assertEqual(solution(12), [9,1,1,1])

    def test_15324(self):
        self.assertEqual(solution(15324), [15129,169,25,1])

if __name__ == '__main__':
    unittest.main()
