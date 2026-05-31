# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            if parent:
                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
                parent.left, parent.right = parent.right, parent.left

        return root