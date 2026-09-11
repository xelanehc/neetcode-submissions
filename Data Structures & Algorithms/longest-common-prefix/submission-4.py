class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        l = 0
        for s in strs:
            l = max(l, len(s))
        
        ret = 0

        for i, c in enumerate(strs[0]):
            for s in strs:
                if s[i] != c:
                    return strs[0][:ret]
            ret = i + 1
        
        return strs[0][:ret]