# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        def dfs(node):
            nonlocal lca

            if not node:
                return
            
            lca = node
            if node is p or node is q:
                return
            elif node.val < p.val and node.val < q.val:
                dfs(node.right)
            elif node.val > p.val and node.val > q.val:
                dfs(node.left)
            else:
                return
        dfs(root)
        return lca