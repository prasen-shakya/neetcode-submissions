# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diamater = 0
        
        def dfs(node):
            nonlocal max_diamater
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            max_diamater = max(max_diamater, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diamater
        