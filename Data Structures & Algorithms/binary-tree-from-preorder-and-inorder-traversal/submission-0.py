# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder, inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            for i, v in enumerate(inorder):
                if v == root_val:
                    break
            root = TreeNode(root_val)
            root.left = construct(preorder[1:i+1], inorder[:i])
            root.right = construct(preorder[i+1:], inorder[i+1:])
            return root
        return construct(preorder, inorder) 


        