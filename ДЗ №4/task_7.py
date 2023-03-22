# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        result = ListNode(values[len(values) // 2])
        current = result

        for el in values[1 + len(values) // 2:]:
            current.next = ListNode(el)
            current = current.next

        return result