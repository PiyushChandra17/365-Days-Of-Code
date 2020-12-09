class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n//5 + self.trailingZeroes(n//5)
    
        #or
        
        r = 0
        while n > 0:
            n //=5
            r += n
        return r