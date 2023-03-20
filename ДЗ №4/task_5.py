# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        binary_list = []

        while head:
            binary_list.append(head.val)
            head = head.next

        return sum(binary_list[i] * 2 ** (len(binary_list) - i - 1) for i in range(len(binary_list)))