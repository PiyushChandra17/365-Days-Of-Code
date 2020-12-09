class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                start_s,start_p = i-1,j-1
                if i==0 and j==0:
                    dp[i][j] =True
                elif i == 0:
                    dp[i][j] = p[start_p]=='*' and dp[i][j-1]
                elif j==0:
                    dp[i][j] = False
                elif p[start_p]=='*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif s[start_s] == p[start_p] or p[start_p]=='?':
                    dp[i][j] = dp[i-1][j-1]
        return dp[len(s)][len(p)]