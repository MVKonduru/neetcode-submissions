class MyHashMap:

    def __init__(self):
        self.hashset = []
        
    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashset)):
            if self.hashset[i][0] == key:
                self.hashset[i][1] = value
                return
        self.hashset.append([key, value])

    def get(self, key: int) -> int:
        for item in self.hashset:
            if item[0] == key:
                return item[1]
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.hashset)):
            if self.hashset[i][0] == key:
                self.hashset.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)