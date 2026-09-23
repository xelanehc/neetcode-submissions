class StockSpanner:

    def __init__(self):
        self.backing = []

    def next(self, price: int) -> int:
        self.backing.append(price)

        i = len(self.backing) - 1

        while i >= 0 and self.backing[i] <= price:
            i -= 1
        
        res = len(self.backing) - i - 1
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)