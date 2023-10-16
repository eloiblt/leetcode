# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest


class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for val in nums:
            if val in dict:
                dict[val] += 1
            else:
                dict[val] = 1

        majority = len(nums) // 2
        for key, value in dict.items():
            if value > majority:
                return key


def check(nums, majorityResult):
    majority = Solution().majorityElement(nums)
    unittest.TestCase().assertEqual(majority, majorityResult)


# nums = [3,2,3]
# majorityResult = 3
# check(nums, majorityResult)


nums = [2, 2, 1, 1, 1, 2, 2]
majorityResult = 2
check(nums, majorityResult)
