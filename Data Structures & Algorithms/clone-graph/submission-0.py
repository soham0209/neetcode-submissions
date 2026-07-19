"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        old2new = {}
        q = [node]
        old2new[node] = Node(node.val)
        while q:
            n = q.pop(0)
            for nei in n.neighbors:
                if nei not in old2new:
                    old2new[nei] = Node(nei.val)
                    q.append(nei)
                old2new[n].neighbors.append(old2new[nei])
        return old2new[node]


        