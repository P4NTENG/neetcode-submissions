# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has_been = []
        curr = head

        while curr:
            if curr in has_been:
                return True
            has_been.append(curr)
            curr = curr.next

        
        return False