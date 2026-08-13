# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque()
        q_queue = deque()
        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            p_curr = p_queue.popleft()
            q_curr = q_queue.popleft()

            if p_curr is None and q_curr is None:
                continue
            if p_curr is None or q_curr is None:
                return False
            if p_curr.val != q_curr.val:
                return False

            p_queue.append(p_curr.left)
            p_queue.append(p_curr.right)
            q_queue.append(q_curr.left)
            q_queue.append(q_curr.right)
        
        return True