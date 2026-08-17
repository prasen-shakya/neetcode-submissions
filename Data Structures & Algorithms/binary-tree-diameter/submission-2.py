# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = -999

        def depth(node):
            if not node:
                return 0
            
            nonlocal res
            
            left_height = depth(node.left)
            right_height = depth(node.right)
            
            res = max(res, left_height+ right_height)

            return 1 + max(left_height, right_height)

        depth(root)

        return res