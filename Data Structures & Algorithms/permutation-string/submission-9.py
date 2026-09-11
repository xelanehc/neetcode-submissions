class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        for c in s1:
            freq1[c] += 1
        l, r = 0, len(s1)
        while r <= len(s2):
            freq2 = defaultdict(int)
            for i in range(l, r):
                freq2[s2[i]] += 1
            if freq1 == freq2:
                return True
            l += 1
            r += 1
        return False