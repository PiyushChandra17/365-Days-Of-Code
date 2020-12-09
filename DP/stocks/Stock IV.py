class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0
        if k >= n//2:
            return sum(i-j for i,j in zip(prices[1:],prices[:-1]) if i-j > 0)
        
        profits = [0]*n
        for j in range(k):
            preprofit = 0
            for i in range(1,n):
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit+profit,profits[i])
                profits[i] = max(profits[i-1],preprofit)
        return profits[-1]