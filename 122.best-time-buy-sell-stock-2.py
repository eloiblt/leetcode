# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest


# Key idea : considering [1, 2, 3], buy 1 sell 3 is equivalent to buy 1 sell 2 + buy 2 sell 3.
# So there is always a profit if price n+1 > price n.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            profit += max((prices[i + 1] - prices[i]), 0)

        return profit


def check(prices, result):
    localResult = Solution().maxProfit(prices)
    unittest.TestCase().assertEqual(localResult, result)


# Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
prices = [7, 1, 5, 3, 6, 4]
result = 7
check(prices, result)

# Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
prices = [1, 2, 3, 4, 5]
result = 4
check(prices, result)

# prices = [7,6,4,3,1
# result = 0
# check(prices, result)
