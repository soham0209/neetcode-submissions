# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self, root):
        if not root:
            return 0
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        self.res = max(self.res, lh+rh)
        return 1 + max(lh, rh)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  
        self.res = 0  
        self.dfs(root)
        return self.res
            
             