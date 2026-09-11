class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.backing = {}
        self.start = Node(-1, -1)
        self.end = Node(-1, -1)
        self.start.next = self.end
        self.end.prev = self.start
    
    def add(self, node):
        self.end.prev.next = node
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.backing:
            return -1
        self.remove(self.backing[key])
        self.add(self.backing[key])
        return self.backing[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.backing:
            toRemove = self.backing[key]
            self.remove(toRemove)
        toAdd = Node(key, value)
        self.backing[key] = toAdd
        self.add(toAdd)
        if len(self.backing) > self.capacity:
            toRemove = self.start.next
            self.remove(toRemove)
            del self.backing[toRemove.key]
