class DLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


def create_doubly_linked_list(numbers: list) -> DLNode:
    head = DLNode(numbers[0])
    current = head

    for num in numbers[1:]:
        prev = current
        current.next = DLNode(num, prev)
        current = current.next

    return head


def get_values_from_doubly_linked_list(head: DLNode) -> list:
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def remove_node(head: DLNode, nodenum: int) -> DLNode:
    result = head
    current = result
    index = 0

    while current:
        if nodenum == 0:
            result = result.next
            break
        elif index == nodenum and current.next:
            left_next = current.next
            right_prev = current.prev
            current.prev.next = left_next
            current.next.prev = right_prev
            break
        elif index <= nodenum and not current.next:
            current.prev.next = None

        index += 1

        current = current.next

    return result


def add_node(head: DLNode, nodenum: int, nodeval: int) -> DLNode:
    result = head
    current = result
    index = 0

    while current:
        if nodenum == 0 or nodenum < index:
            result = DLNode(val=nodeval, next=current)
            break
        elif index == nodenum:
            new = DLNode(val=nodeval, prev=current.prev, next=current)
            current.prev.next = new
            current.prev = new
            break
        elif index < nodenum and not current.next:
            current.next = DLNode(val=nodeval, prev=current)
            break

        index += 1

        current = current.next

    return result


def inverse_list(head: DLNode) -> DLNode:
    current = head
    prev = None

    while current:
        nxt = current.next
        prev = current.prev

        current.prev = nxt
        current.next = prev

        current = nxt

    return prev.prev
