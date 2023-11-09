# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price > min_price:
                continue
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     maxProfit = 0
    #     minValue = prices[0]
    #     currentMaxValue = sys.maxsize

    #     i = 0
    #     while i < len(prices) - 1:
    #         dayValue = prices[i]
    #         if dayValue > minValue or dayValue == currentMaxValue:
    #             i += 1
    #             continue
    #         minValue = dayValue

    #         currentMaxValue = max(list(set(prices[i + 1 :])))
    #         localProfit = currentMaxValue - dayValue
    #         if localProfit > maxProfit:
    #             maxProfit = localProfit
    #         i += 1
    #     return maxProfit


def check(prices, result):
    localResult = Solution().maxProfit(prices)
    unittest.TestCase().assertEqual(localResult, result)


prices = [7, 1, 5, 3, 6, 4]
result = 5
check(prices, result)

# prices = [7, 6, 4, 3, 1]
# result = 0
# check(prices, result)

# prices = [2, 4, 1]
# result = 2
# check(prices, result)
