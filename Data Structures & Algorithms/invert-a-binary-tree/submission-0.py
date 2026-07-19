# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(root):
            if not root:
                return root
            tmp = recurse(root.left)
            tmp2 = recurse(root.right)
            root.right = tmp
            root.left = tmp2
            return root
        return recurse(root)
            
        