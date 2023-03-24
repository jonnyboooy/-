# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        l1 = 0
        l2 = 0

        while l1 != len(nums1):
            while l2 != len(nums2):
                if nums1[l1] == nums2[l2] and nums1[l1] not in inter:
                    inter.append(nums1[l1])
                l2 += 1

            l2 = 0
            l1 += 1

        return inter