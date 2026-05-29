# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # tail 구하기
        curr = head
        while curr and curr.next:
            curr = curr.next
        tail = curr

        # circular linked list로 만들기
        if tail:
            tail.next = head

        # n칸 떨어진 노드 구하기
        curr = head
        for i in range(n - 1):
            if curr:
                curr = curr.next

        n_1th_node = curr
        if n_1th_node:
            nth_node = n_1th_node.next
        # 다시 연결 끊기
        if tail:
            tail.next = None
        if head and head is nth_node:
            head = head.next
        if nth_node and n_1th_node:
            n_1th_node.next = nth_node.next

        return head