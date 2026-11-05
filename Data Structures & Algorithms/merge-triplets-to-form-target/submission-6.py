class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x0, y0, z0 = target
        xt = yt = zt = False
        for x, y, z in triplets:
            if x <= x0 and y <= y0 and z <= z0:
                xt |= x == x0
                yt |= y == y0 
                zt |= z == z0
            if xt and yt and zt:
                return True
        
        return False