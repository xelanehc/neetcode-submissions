class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, cur):
            if left == right and right == n:
                res.append(cur)
                return
            
            if left < right or left > n:
                return
            
            cur += "("
            dfs(left + 1, right, cur)
            cur = cur[:-1]
            cur += ")"
            dfs(left, right + 1, cur)
        
        dfs(0, 0, "")
        return res