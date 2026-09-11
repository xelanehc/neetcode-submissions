class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countlist = [0] * 26
        for i in range(len(s)):
            countlist[ord(s[i]) - ord('a')] += 1
            countlist[ord(t[i]) - ord('a')] -= 1
        for i in countlist:
            if i != 0:
                return False
        return True