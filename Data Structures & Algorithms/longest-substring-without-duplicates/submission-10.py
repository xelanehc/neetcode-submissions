class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in window:
                while l < r and s[r] in window:
                    window.remove(s[l])
                    l += 1
            res = max(res, r - l + 1)
            window.add(s[r])

        return res
