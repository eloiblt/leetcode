# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest


class Solution:
    ## best solution. We calculate the max index where we can go.
    ## as we can always jump less further, if we can iterate all items without passing reachable it means True
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, i + nums[i])

        return True

    # my solution
    # def canJump(self, nums: List[int]) -> bool:
    #     testedIndexes = set()

    #     def testJump(position):
    #         # from biggest jump to lowest (0)
    #         for potentialJump in range(nums[position], -1, -1):
    #             endIndex = position + potentialJump
    #             if endIndex in testedIndexes:
    #                 continue

    #             if endIndex == len(nums) - 1:
    #                 return True

    #             if potentialJump == 0 or endIndex > len(nums) - 1:
    #                 continue

    #             jumpResult = testJump(endIndex)
    #             if jumpResult:
    #                 return True
    #             else:
    #                 testedIndexes.add(endIndex)

    #         return False

    #     return testJump(0)


def check(nums, result):
    localResult = Solution().canJump(nums)
    unittest.TestCase().assertEqual(localResult, result)


nums = [2, 3, 1, 1, 4]
result = True
check(nums, result)

nums = [3, 2, 1, 0, 4]
result = False
check(nums, result)

nums = [0]
result = True
check(nums, result)

nums = [1]
result = True
check(nums, result)

nums = [2, 5, 0, 0]
result = True
check(nums, result)
