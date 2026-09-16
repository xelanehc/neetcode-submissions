class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) and not self.isAlpha(s[l]):
                l += 1
            while r >= 0 and not self.isAlpha(s[r]):
                r -= 1
            if l >= len(s) or r < 0:
                break
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
    
    def isAlpha(self, c):
        return (ord('0') <= ord(c) <= ord('9')
            or ord('A') <= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z'))