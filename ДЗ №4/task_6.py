# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        result = head
        cur = result
        b = result.next

        while cur:
            cur.val += b.val

            if b.next.next and b.next.val != 0:
                b = b.next
            elif b.next.next and b.next.val == 0:
                cur.next = b.next
                cur = cur.next
                b = b.next.next
            else:
                cur.next = None
                cur = cur.next

        return result