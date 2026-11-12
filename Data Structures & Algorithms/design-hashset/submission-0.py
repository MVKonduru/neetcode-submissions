class MyHashSet:

    def __init__(self):
        self.hashset = []
        
    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def contains(self, key: int) -> int:
        if key in self.hashset:
            return True
        else:
            return False
        
    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)