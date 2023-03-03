# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        values = [head.val]

        while head.next:
            if not head.val == head.next.val:
                values.append(head.next.val)

            head = head.next

        result = ListNode(values[0])
        current = result

        for el in values[1:]:
            current.next = ListNode(el)
            current = current.next

        return result
