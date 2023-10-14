# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
import unittest

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if i2 < 0 or (i1 >= 0 and nums1[i1] >= nums2[i2]):
                nums1[i] = nums1[i1]
                i1 = i1 - 1
            else:
                nums1[i] = nums2[i2]
                i2 = i2 - 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Solution().merge(nums1, m, nums2, n)
unittest.TestCase().assertEqual(nums1, [1,2,2,3,5,6])

nums1 = [1]
m = 1
nums2 = []
n = 0

Solution().merge(nums1, m, nums2, n)
unittest.TestCase().assertEqual(nums1, [1])

nums1 = [0]
m = 0
nums2 = [1]
n = 1

Solution().merge(nums1, m, nums2, n)
unittest.TestCase().assertEqual(nums1, [1])
