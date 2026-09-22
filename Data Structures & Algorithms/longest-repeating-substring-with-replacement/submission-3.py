class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            mp[s[r]] += 1

            sub = r - l + 1

            if sub - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            else:
                res = max(res, sub)
        
        return res