# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = {val:idx for idx, val in enumerate(inorder)}
        self.root_idx = 0
        def construct(l, r):
            if l > r:
                return None
            root_val = preorder[self.root_idx]
            self.root_idx += 1
            mid = self.idx[root_val]
            root = TreeNode(root_val)
            root.left = construct(l, mid-1)
            root.right = construct(mid+1, r)
            return root
        return construct(0, len(preorder)-1) 


        