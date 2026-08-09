class MyHashSet:

    def __init__(self):
        self.contents = set()

    def add(self, key: int) -> None:
        self.contents.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.contents.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.contents


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)