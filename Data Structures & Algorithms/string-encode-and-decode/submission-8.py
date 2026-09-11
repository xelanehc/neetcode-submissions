class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + '#' + s
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            ret.append(s[l:r])
            l = r
        return ret
