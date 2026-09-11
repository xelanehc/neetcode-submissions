class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(l, r):
            if r == len(s):
                if l == r:
                    res.append(cur.copy())
                return
            
            if isPalindrome(l, r):
                cur.append(s[l : r + 1])
                dfs(r + 1, r + 1)
                cur.pop()
            
            dfs(l, r + 1)


        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        dfs(0, 0)
        return res