# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r != len(nums) - 1:
            r += 1
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

        return l + 1
