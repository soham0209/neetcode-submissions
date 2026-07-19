"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(head.val)
        node_dict = {head: new_head}
        tmp = head
        l2 = new_head
        while tmp:
            next_ptr = tmp.next
            random_ptr = tmp.random
            if next_ptr:
                if next_ptr not in node_dict:
                    node_dict[next_ptr] = Node(next_ptr.val)
                l2.next = node_dict[next_ptr]
            else:
                l2.next = None
            if random_ptr:
                if random_ptr not in node_dict:
                    node_dict[random_ptr] = Node(random_ptr.val)
                l2.random = node_dict[random_ptr]
            else:
                l2.random = None
            tmp = next_ptr
            l2 = l2.next
        return new_head 