class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = defaultdict(int)
        dt = defaultdict(int)
        for i in s:
            ds[i] += 1
        for i in t:
            dt[i] += 1
        for k in ds.keys():
            if ds[k] != dt[k]:
                return False
        return True