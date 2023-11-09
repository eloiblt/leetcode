# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import unittest


class Solution:
    # best solution
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            a = nums.pop()
            nums.insert(0, a)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            nums.insert(0, nums[-1])
            del nums[-1]
            i += 1
        return nums

    # manual, slower
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        while i < k:
            j = 0
            while j < len(nums):
                oldValue = nums[j]
                nums[j] = nums[-1] if j == 0 else prevValue
                prevValue = oldValue
                j += 1
            i += 1
        return nums


def check(array, k, result):
    localResult = Solution().rotate(array, k)
    unittest.TestCase().assertEqual(localResult, result)


array = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = [5, 6, 7, 1, 2, 3, 4]
check(array, k, result)


array = [-1, -100, 3, 99]
k = 2
result = [3, 99, -1, -100]
check(array, k, result)
