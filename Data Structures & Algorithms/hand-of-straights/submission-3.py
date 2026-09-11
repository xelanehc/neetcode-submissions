class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = defaultdict(int)
        for h in hand:
            d[h] += 1
        
        for h in hand:
            start = h
            while d[start - 1]:
                start -= 1
            while start <= h:
                while d[start]:
                    for i in range(start, start + groupSize):
                        if not d[i]:
                            return False
                        d[i] -= 1
                start += 1
            
        return True