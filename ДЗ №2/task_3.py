# https://leetcode.com/problems/middle-of-the-linked-list/
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
