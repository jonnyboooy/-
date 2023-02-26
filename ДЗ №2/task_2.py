# https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        for i in range(len(values)):
            if values[i] != values[len(values) - i - 1]:
                return False

        return True
