# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        c = res

        while c:
            if c.next and c.next.val == val:
                c.next = c.next.next
            else:
                c = c.next

        return res.next