class RandomizedSet:

    def __init__(self):
        self.my_map = {}
        self.my_arr = []

    def insert(self, val: int) -> bool:
        if val in self.my_map:
            return False

        self.my_arr.append(val)
        self.my_map[val] = len(self.my_arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.my_map:
            return False

        index = self.my_map[val]
        self.my_map[self.my_arr[-1]] = index
        self.my_arr[index] = self.my_arr[-1]
        self.my_arr.pop()
        del self.my_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.my_arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()