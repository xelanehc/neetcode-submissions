class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        l = min(len(word1), len(word2))
        i = 0
        while i < l:
            s += word1[i] + word2[i]
            i += 1
        
        if len(word1) > len(word2):
            s += word1[i:]
        else:
            s += word2[i:]
        
        return s