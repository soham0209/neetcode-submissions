# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, count):
            if not node:
                return count, None
            
            # Process left subtree
            count, left_result = dfs(node.left, count)
            if left_result is not None:
                return count, left_result
            
            # Process current node
            count -= 1
            if count == 0:
                return count, node.val
            
            # Process right subtree
            return dfs(node.right, count)
    
        _, result = dfs(root, k)
        return result


        
            
        