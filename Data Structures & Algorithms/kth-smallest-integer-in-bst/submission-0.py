# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(node, ans):
            if not node:
                return ans
            ans_left = in_order(node.left, ans)
            ans_right = in_order(node.right, ans)
            return ans_left + [node.val] + ans_right
        sorted_list = in_order(root, [])
        return sorted_list[k-1]
        