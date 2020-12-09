class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        dp,ans = 0,0
        
        for i in range(0,len(nums)-1):
            q = nums[i+1]-nums[i]
            
            dp = max(dp+q,q)
            ans =max(ans,dp)
            
        return ans
        
    def maxProfit(self, prices):
    
        fb, fs = float('inf'), 0
        for price in prices:
            fb = min(fb, price) # keep minimal
            fs = max(fs, price-fb) # compute max difference
        return fs