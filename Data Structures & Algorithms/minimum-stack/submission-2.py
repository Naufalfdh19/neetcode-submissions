from sortedcontainers import SortedDict

class MinStack:

    def __init__(self):
        self.stack = []
        self.hashmap = SortedDict()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.hashmap:
            self.hashmap[val] = 0
        self.hashmap[val] += 1

    def pop(self) -> None:
        if self.stack:
            num = self.stack.pop()
            if num in self.hashmap:
                self.hashmap[num] -= 1
            if self.hashmap[num] == 0:
                del self.hashmap[num]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

        return None

    def getMin(self) -> int:
        return min(self.hashmap)
        
