# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:

#     1 <= n <= 45

import unittest


def count(n: int) -> int:
    x = 1
    y = 1

    for i in  range(n - 1):
        temp = x
        x = x + y
        y = temp

    return x

class Test(unittest.TestCase):
    def test_00(self):
        self.assertEqual(count(1), 1)

    def test_02(self):
        self.assertEqual(count(2), 2)

    def test_03(self):
        self.assertEqual(count(3), 3)

    def test_04(self):
        self.assertEqual(count(4), 5)

    def test_05(self):
        self.assertEqual(count(5), 8)

    def test_06(self):
        self.assertEqual(count(6), 13)

if __name__ == '__main__':
    unittest.main()
