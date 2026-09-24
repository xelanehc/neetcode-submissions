class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        valFreq = self.freq.get(val, 0) + 1
        self.freq[val] = valFreq

        if valFreq > self.maxFreq:
            self.maxFreq = valFreq
            self.stacks[self.maxFreq] = []
        
        self.stacks[valFreq].append(val)

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