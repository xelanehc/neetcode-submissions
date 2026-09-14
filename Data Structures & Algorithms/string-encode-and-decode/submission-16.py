class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            ret.append(str(len(s)))
            ret.append("#")
            ret.append(s)
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            ret.append(s[i:j])
            i = j
        
        return ret