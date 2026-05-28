# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        curr = dummy

        while curr and head:
            tail_1 = head
            while tail_1 and tail_1.next and tail_1.next.next:
                tail_1 = tail_1.next
            tail = tail_1.next
            tail_1.next = None

            curr.next = head
            curr = curr.next
            head = head.next
            curr.next = tail
            curr = curr.next

        # return dummy.next