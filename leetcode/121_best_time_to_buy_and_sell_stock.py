import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit = max(prices[sell] - prices[buy], maxProfit)
            else:
                buy = sell
            sell += 1

        return maxProfit


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution.maxProfit(self, [7, 1, 5, 3, 6, 4]), 5)

    def test_2(self):
        self.assertEqual(Solution.maxProfit(self, [7, 6, 4, 3, 1]), 0)


if __name__ == '__main__':
    unittest.main()

