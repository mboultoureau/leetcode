class MyQueue:

    def __init__(self):
        self.reversed = False
        self.stack_normal = []
        self.stack_reversed = []

    def reverse_stack(self):
        if self.reversed == True:
            while len(self.stack_reversed) != 0:
                self.stack_normal.append(self.stack_reversed[-1])
                self.stack_reversed.pop()
        else:
            while len(self.stack_normal) != 0:
                self.stack_reversed.append(self.stack_normal[-1])
                self.stack_normal.pop()

        self.reversed = not self.reversed

    def push(self, x: int) -> None:
        if self.reversed:
            self.reverse_stack()

        self.stack_normal.append(x)

    def pop(self) -> int:
        if not self.reversed:
            self.reverse_stack()

        return self.stack_reversed.pop()

    def peek(self) -> int:
        if not self.reversed:
            self.reverse_stack()

        return self.stack_reversed[-1]

    def empty(self) -> bool:
        if not self.reversed:
            return len(self.stack_normal) == 0
        else:
            return len(self.stack_reversed) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()