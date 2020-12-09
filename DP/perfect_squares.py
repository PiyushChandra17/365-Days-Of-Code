class Solution:
    def numSquares(self, n: int) -> int:
        
        coins = [i**2 for i in range(1,int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for c in coins:
            for i in range(1,n+1):
                if i >= c:
                    dp[i] = min(dp[i],dp[i-c]+1)
        return dp[-1]