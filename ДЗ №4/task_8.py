# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ha = headA
        hb = headB
        counter_a = 0
        counter_b = 0

        while ha or hb:
            if ha:
                counter_a += 1
                ha = ha.next
            if hb:
                counter_b += 1
                hb = hb.next

        count = abs(counter_a - counter_b)

        ha, hb = headA, headB

        while ha:

            if count > 0:
                if counter_a < counter_b:
                    hb = hb.next
                else:
                    ha = ha.next

                count -= 1
            elif ha is hb:
                return ha
            else:
                ha = ha.next
                hb = hb.next
        return