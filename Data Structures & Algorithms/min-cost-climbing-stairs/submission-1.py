class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        T = [0] * (n + 1)
        for i in range(2, n + 1):
            T[i] = min(cost[i - 1] + T[i - 1], cost[i - 2] + T[i - 2])
        return T[n]
