class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = {}
        tD = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sD[s[i]] = sD.get(s[i], 0) + 1
            tD[t[i]] = tD.get(t[i], 0) + 1
        for k in sD.keys():
            if k not in tD or sD[k] != tD[k]:
                return False
        return True
        