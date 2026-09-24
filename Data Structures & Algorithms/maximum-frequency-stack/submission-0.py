class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        cval = 1 + self.freq.get(val, 0)
        self.freq[val] = cval
        if cval > self.maxFreq:
            self.maxFreq = cval
            self.stacks[cval] = []
        self.stacks[cval].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.stacks[self.maxFreq]:
            self.maxFreq -= 1
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()