class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
        
        have, need = 0, len(freqT)

        l = 0
        freqS = {}
        res, resLen = [-1, -1], float('inf')
        for r in range(len(s)):
            freqS[s[r]] = freqS.get(s[r], 0) + 1

            if s[r] in freqT and freqS[s[r]] == freqT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]

                freqS[s[l]] -= 1

                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""