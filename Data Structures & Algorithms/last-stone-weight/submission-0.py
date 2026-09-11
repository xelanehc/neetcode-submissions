class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            x = stones[-1]
            stones.pop()
            y = stones[-1]
            stones.pop()
            if x > y:
                stones.append(x - y)
            stones = sorted(stones)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
            
