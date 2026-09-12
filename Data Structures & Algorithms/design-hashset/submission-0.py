class MyHashSet:

    def __init__(self):
        self.backing = []

    def add(self, key: int) -> None:
        self.backing.append(key)

    def remove(self, key: int) -> None:
        copy = []
        for i, n in enumerate(self.backing):
            if n != key:
                copy.append(n)
        self.backing = copy

    def contains(self, key: int) -> bool:
        for n in self.backing:
            if n == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)