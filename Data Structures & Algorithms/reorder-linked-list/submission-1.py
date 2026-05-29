# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while slow and fast and slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next if slow else None
        if slow:
            slow.next = None

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        first = head
        second = reverseList(middle)

        while second:
            if first:
                next1 = first.next
            next2 = second.next
            if first:
                first.next = second
            second.next = next1
            first = next1
            second = next2
