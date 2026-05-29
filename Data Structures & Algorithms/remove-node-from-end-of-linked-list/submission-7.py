# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()  # 뒤에서 n+1번째
        dummy.next = head
        n_1th_node = dummy
        offset = 0
        while curr:
            if n_1th_node and offset >= n:
                n_1th_node = n_1th_node.next
            curr = curr.next
            offset += 1
        if n_1th_node:
            nth_node = n_1th_node.next
        if n_1th_node and nth_node:
            n_1th_node.next = nth_node.next

        return dummy.next