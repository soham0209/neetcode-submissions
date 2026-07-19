
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.nodemap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
    
    def insert(self, node):
        left, end = self.tail.prev, self.tail
        left.next = node
        node.prev = left
        node.next = end
        end.prev = node
    
    def get(self, key: int) -> int:
        if key in self.nodemap:
            val = self.nodemap[key].val
            self.remove(self.nodemap[key])
            self.insert(self.nodemap[key])
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodemap:
            self.remove(self.nodemap[key])
        self.nodemap[key] = Node(key, value)
        self.insert(self.nodemap[key])
        if len(self.nodemap) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.nodemap[lru.key]
            


        
