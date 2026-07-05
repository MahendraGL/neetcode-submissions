class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[0]
        two = cost[1]

        for i in range(2, len(cost)):
            curr = min(one,two) + cost[i]
            one = two
            two = curr
        return min(one,two)