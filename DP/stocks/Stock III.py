class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fb,fp,sb,sp = float('inf'),0,float('inf'),0
        
        for price in prices:
            fb = min(fb,price)
            fp = max(fp,price-fb)
            sb = min(sb,price-fp)
            sp = max(sp,price-sb)
        return sp