class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freqt = {}
        for c in t:
            freqt[c] = freqt.get(c, 0) + 1
        
        have, need = 0, len(freqt)        
        l = 0
        res, resLen = [-1, -1], float('inf')
        freqs = {}

        for r in range(len(s)):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)

            if s[r] in freqt and freqs[s[r]] == freqt[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                index = ord(s[l]) - ord('a')
                freqs[s[l]] -= 1
                if s[l] in freqt and freqs[s[l]] < freqt[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0] : res[1] + 1] if resLen != float('inf') else ""
