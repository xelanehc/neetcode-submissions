class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        d = Counter(hand)
        
        for h in hand:
            if d[h]:
                for i in range(h, h + groupSize):
                    if not d[i]:
                        return False
                    d[i] -= 1
        return True