class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        size = len(self.prefix) - 1

        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[size] * num)

    def getProduct(self, k: int) -> int:
        size = len(self.prefix) - 1

        if k > size:
            return 0

        return self.prefix[size] // self.prefix[size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)