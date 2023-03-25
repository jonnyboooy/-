# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = head
        c = res
        l = None

        while c:
            if c.val == val and l == None:
                r = c.next
                c.next = None
                res = r
                c = res
            elif c.val == val and l != None:
                r = c.next
                l.next = r
                c.next = None
                c = r
            else:
                l = c
                c = c.next

        return res