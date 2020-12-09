class Solution:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda x,y: x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
        #return reduce(lambda x,y: x*26+y, [ord(c)-64 for c in list(s)])