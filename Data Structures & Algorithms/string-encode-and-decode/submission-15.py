class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            ret.append(str(len(s)))
            ret.append("#")
            ret.append(s)
        
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            temp = s[i:j]
            ret.append(temp)
            i = j
        return ret