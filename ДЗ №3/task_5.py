# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l1 = 0
        l2 = 0

        while l2 != len(nums):
            if nums[l1] == 0 and nums[l2] != 0:
                buff = nums[l1]
                nums[l1] = nums[l2]
                nums[l2] = buff
                l1 += 1

            if nums[l1] != 0:
                l1 += 1

            l2 += 1
