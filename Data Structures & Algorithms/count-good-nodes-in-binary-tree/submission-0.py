# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = [(root, root.val)]
        count = 0
        while q:
            node, max_in_this_path = q.pop(0)
            if node.val >= max_in_this_path:
                count += 1
            if node.left:
                q.append((node.left, max(node.val, max_in_this_path)))
            if node.right:
                q.append((node.right, max(node.val, max_in_this_path)))
        return count
            

        