class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for c in t:
            countT[c] += 1
        
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            cur = s[r]
            countS[cur] += 1

            if cur in countT and countT[cur] == countS[cur]:
                have += 1
            
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                
                countS[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > countS[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""