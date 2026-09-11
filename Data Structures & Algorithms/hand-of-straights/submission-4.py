class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1
        
        for h in hand:
            start = h
            while freq[start - 1]:
                start -= 1
            
            while start <= h:
                while freq[start]:
                    for i in range(start, start + groupSize):
                        if not freq[i]:
                            return False
                        freq[i] -= 1
                start += 1
        return True