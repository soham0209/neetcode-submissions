# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            rightMost = None
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)
                rightMost = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rightMost:
                res.append(rightMost.val)
        return res
                

        