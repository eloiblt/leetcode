# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        while i < len(nums):
            j = i + 2 if i + 1 < len(nums) and nums[i + 1] == nums[i] else i + 1
            while j < len(nums) and nums[j] == nums[i]:
                del nums[j]
            i = j
        return i


def check(nums, kResult, numsResult):
    k = Solution().removeDuplicates(nums)
    unittest.TestCase().assertEqual(k, kResult)
    unittest.TestCase().assertEqual(nums, numsResult)


nums = [1, 1, 1, 1, 2, 3, 3, 3, 4, 4]
kResult = 7
numsResult = [1, 1, 2, 3, 3, 4, 4]
check(nums, kResult, numsResult)

nums = [1, 1, 1, 2, 2, 3]
kResult = 5
numsResult = [1, 1, 2, 2, 3]
check(nums, kResult, numsResult)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
kResult = 7
numsResult = [0, 0, 1, 1, 2, 3, 3]
check(nums, kResult, numsResult)
