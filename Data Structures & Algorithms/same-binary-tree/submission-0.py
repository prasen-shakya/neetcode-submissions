# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree_1, tree_2):
            if not tree_1 and not tree_2:
                return True

            if (tree_1 and not tree_2) or (tree_2 and not tree_1):
                return False
            
            if tree_1.val != tree_2.val:
                return False
            
            return dfs(tree_1.left, tree_2.left) and dfs(tree_1.right, tree_2.right)
            
        return dfs(p, q)