class StockSpanner:

    def __init__(self):
        self.backing = []

    def next(self, price: int) -> int:
        res = 1
        
        while self.backing and self.backing[-1][0] <= price:
            res += self.backing[-1][1]
            self.backing.pop()
        
        self.backing.append((price, res))
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)