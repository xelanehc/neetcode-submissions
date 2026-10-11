class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.remove(self.d[key])
        self.insert(self.d[key])
        return self.d[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = Node(key, value)
        self.insert(self.d[key])

        if len(self.d) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.d[lru.key]

        