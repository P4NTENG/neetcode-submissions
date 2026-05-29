# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and head.next is None:
            head = head.next
        curr = head
        n_1th_node = head
        offset = 0
        while curr and curr.next:
            if n_1th_node and offset >= n:
                n_1th_node = n_1th_node.next
            curr = curr.next
            offset += 1
        if n_1th_node:
            nth_node = n_1th_node.next
        if n_1th_node and nth_node:
            n_1th_node.next = nth_node.next

        return head