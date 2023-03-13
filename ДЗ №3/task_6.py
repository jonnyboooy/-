# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        duplicates_count = 0

        while r != len(nums):
            if nums[l] == nums[r] and duplicates_count < 2:
                r += 1
                duplicates_count += 1
            elif nums[l] == nums[r] and duplicates_count >= 2:
                nums.pop(r)
            elif nums[l] != nums[r]:
                duplicates_count = 1
                l = r
                r += 1
