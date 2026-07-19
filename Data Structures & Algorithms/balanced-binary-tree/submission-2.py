# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            lh, l_bal = dfs(root.left)
            rh, r_bal = dfs(root.right)
            flag = l_bal and r_bal and abs(lh-rh) <= 1
            return 1 + max(lh, rh), flag
        h, b = dfs(root)
        return b
        