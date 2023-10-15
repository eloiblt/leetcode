# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
import unittest

"""
Logique
Il faut retourner le parametre nums1
On parcourt les 2 tableaux de la fin vers le début car on est sur de n'avoir que des valeurs exploitables
Si on faisait l'inverse, on aurait des zeros à la fin de nums1. En plus, ici m est l'index de la dernière valeur exploitable
while i2 >= 0 car si les 2 tableaux sont triés, on est ok dès lors qu'on a traité tous les élements de nums2
"""

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
        nums1Index = m + n - 1

        while i2 >= 0:
            if i1 >= 0 and nums1[i1] >= nums2[i2]:
                nums1[nums1Index] = nums1[i1]
                i1 = i1 - 1
            else:
                nums1[nums1Index] = nums2[i2]
                i2 = i2 - 1
            nums1Index -= 1

def check(nums1, m, nums2, n, result):
    Solution().merge(nums1, m, nums2, n)
    unittest.TestCase().assertEqual(nums1, result)

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
result = [1,2,2,3,5,6]

check(nums1, m, nums2, n, result)

nums1 = [1]
m = 1
nums2 = []
n = 0
result = [1]

check(nums1, m, nums2, n, result)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
result = [1]

check(nums1, m, nums2, n, result)
