class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqs = defaultdict(int)
        freqt = defaultdict(int)
        for i in range(len(s)):
            freqs[s[i]] += 1
            freqt[t[i]] += 1
        
        return freqs == freqt