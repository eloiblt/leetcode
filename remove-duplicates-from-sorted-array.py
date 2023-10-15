# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
import unittest


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                del nums[j]
            i += 1
        return i


def check(nums, kResult, numsResult):
    k = Solution().removeDuplicates(nums)
    unittest.TestCase().assertEqual(k, kResult)
    unittest.TestCase().assertEqual(nums, numsResult)


nums = [1, 1, 2]
kResult = 2
numsResult = [1, 2]
check(nums, kResult, numsResult)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
kResult = 5
numsResult = [0, 1, 2, 3, 4]
check(nums, kResult, numsResult)

nums = [1, 1]
kResult = 1
numsResult = [1]
check(nums, kResult, numsResult)
