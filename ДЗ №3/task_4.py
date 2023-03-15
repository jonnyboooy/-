# https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        l1 = 0
        l2 = 0
        min_index = 0

        while l1 != len(nums1):
            while l2 != len(nums2):
                if nums2[l2] <= nums2[min_index]:
                    min_index = l2

                l2 += 1

            if nums1[l1] == 0 and l1 >= m:
                nums1[l1], nums2[min_index] = nums2[min_index], 201
            elif nums2[min_index] < nums1[l1]:
                nums1[l1], nums2[min_index] = nums2[min_index], nums1[l1]

            l1 += 1
            l2 = 0
