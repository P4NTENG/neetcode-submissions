# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        else:
            smaller, bigger = list1, list2
            head = bigger if smaller and bigger and smaller.val > bigger.val else smaller

            while smaller and bigger:
                if smaller.val > bigger.val:
                    smaller, bigger = bigger, smaller
                next_node = smaller.next
                if next_node is None or next_node.val >= bigger.val:
                    smaller.next = bigger
                smaller = next_node

            return head