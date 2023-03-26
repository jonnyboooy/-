# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = head
        r = head
        prev = None
        fast = head

        while r:
            r = r.next

            if not fast.next:
                l = prev
                break
            elif not fast.next.next:
                l.next = prev
                break
            else:
                fast = fast.next.next

                nxt = l.next
                l.next = prev
                prev = l
                l = nxt

        while r:
            if l.val != r.val:
                return False

            l = l.next
            r = r.next

        return True