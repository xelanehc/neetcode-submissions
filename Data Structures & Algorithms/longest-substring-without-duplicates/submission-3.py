class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        freq = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            while r < len(s) and s[r] not in freq:
                freq.add(s[r])
                r += 1
            res = max(res, r - l)
            while r < len(s) and s[r] in freq:
                freq.remove(s[l])
                l += 1
        return res