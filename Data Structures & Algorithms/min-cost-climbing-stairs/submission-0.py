class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = cost + [0]

        for i in range(len(min_cost) - 3, -1, -1):
            min_cost[i] = min(min_cost[i] + min_cost[i + 1], min_cost[i] + min_cost[i + 2])

        return min(min_cost[0], min_cost[1])
            

