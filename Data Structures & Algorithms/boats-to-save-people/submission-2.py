class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0] * (max(people) + 1)

        for p in people:
            count[p] += 1
        
        p_i, i = 0, 1
        while p_i < len(people):
            while count[i] == 0:
                i += 1
            people[p_i] = i
            count[i] -= 1
            p_i += 1
        
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            remaining = limit - people[r]
            res += 1
            r -= 1
            if l <= r and remaining >= people[l]:
                l += 1
            
        return res