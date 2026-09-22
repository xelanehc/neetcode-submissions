class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for a in asteroids:
            while res and a < 0 and res[-1] > 0:
                diff = res[-1] + a
                if diff < 0:
                    res.pop()
                elif diff > 0:
                    a = 0
                else:
                    res.pop()
                    a = 0
            if a:
                res.append(a)
        
        return res