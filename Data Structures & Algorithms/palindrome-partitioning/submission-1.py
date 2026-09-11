class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(cur.copy())
                return
            
            if palindrome(i, j):
                cur.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                cur.pop()
            dfs(i, j + 1)

        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        dfs(0, 0)
        return res