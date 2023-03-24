# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        l = 0
        r = len(values) - 1

        while l < r:
            if values[l] != values[r]:
                return False

            l += 1
            r -= 1

        return True