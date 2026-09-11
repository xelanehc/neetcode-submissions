class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        freqS, freqT = {}, {}

        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
        
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(freqT)
        l = 0
        for r in range(0, len(s)):
            c = s[r]
            freqS[c] = freqS.get(c, 0) + 1
            if c in freqT and freqS[c] == freqT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                freqS[s[l]] -= 1
                if s[l] in freqT and freqT[s[l]] > freqS[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""