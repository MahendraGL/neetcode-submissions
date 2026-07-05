class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[0], cost[1]]
        n = len(cost)

        for i in range(2, n):
            minCost.append(cost[i] + min(minCost[i-1], minCost[i-2]))

        return min(minCost[n-1], minCost[n-2])

        