class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        
        dp = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1 + min(dfs(i + 1, j + 1), dfs(i, j + 1), dfs(i + 1, j))
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            dp[(i, j)] = res
            return dp[(i, j)]
        
        return dfs(0, 0)