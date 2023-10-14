# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = len([nums[i] for i in range(len(nums)) if nums[i] != val])

        i = 0
        while len(nums) != k:
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return k


def check(nums, val, kResult, numsResult):
    k = Solution().removeElement(nums, val)
    unittest.TestCase().assertEqual(k, kResult)
    unittest.TestCase().assertEqual(nums.sort(), numsResult.sort())


nums = [2]
val = 3
kResult = 1
numsResult = [2]
check(nums, val, kResult, numsResult)


nums = [3, 2, 2, 3]
val = 3
kResult = 2
numsResult = [2, 2]
check(nums, val, kResult, numsResult)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
kResult = 5
numsResult = [0, 1, 4, 0, 3]
check(nums, val, kResult, numsResult)
