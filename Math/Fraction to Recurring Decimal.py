class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n,remainder = divmod(abs(numerator),abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        stack = []
        result = [sign+str(n),'.']
        
        while remainder not in stack:
            stack.append(remainder)
            n,remainder = divmod(10*remainder,abs(denominator))
            result.append(str(n))
            
        idx = stack.index(remainder)
        result.insert(idx+2,'(')
        result.append(')')
        return ''.join(result).replace('(0)','').rstrip('.')
        