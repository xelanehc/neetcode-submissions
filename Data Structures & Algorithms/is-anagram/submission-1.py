class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        for i in range(len(slist)):
            if (slist[i] != tlist[i]):
             return False
        return True
        