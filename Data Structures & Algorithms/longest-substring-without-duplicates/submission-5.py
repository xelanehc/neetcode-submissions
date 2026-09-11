class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        res = 0
        l = 0
        for r in range(len(s)):
            while d1[s[r]] > 0:
                d1[s[l]] -= 1
                l += 1
            d1[s[r]] += 1
            res = max(res, r - l + 1)

        return res