class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = prices[0]
        suffix[n-1] = prices[n-1]
        
        for i in range(1, n):
            prefix[i] = min(prefix[i-1], prices[i])

        for j in range(n-2, -1, -1):
            suffix[j] = max(suffix[j+1], prices[j])
        
        for k in range(n-1):
            curr_profit = suffix[k] - prefix[k]
            profit = max(curr_profit, profit)
        return profit