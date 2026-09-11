class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "___"
        build = ""
        for i in range(len(strs)):
            build += strs[i]
            if i != len(strs) - 1:
                build += "|"
        return build
    def decode(self, s: str) -> List[str]:
        if s == "___":
            return []
        elif len(s) == 0:
            return [""]
        return s.split("|")