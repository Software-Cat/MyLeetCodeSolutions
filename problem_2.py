from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        while l1:
            n1.insert(0, str(l1.val))
            l1 = l1.next

        n2 = []
        while l2:
            n2.insert(0, str(l2.val))
            l2 = l2.next

        n1 = int("".join(n1))
        n2 = int("".join(n2))

        s = n1 + n2

        # Before head is the node before the first node that acts as a dummy
        current = beforeHead = ListNode()
        for digit in reversed([int(d) for d in str(s)]):
            current.next = ListNode(digit)
            current = current.next

        return beforeHead.next
