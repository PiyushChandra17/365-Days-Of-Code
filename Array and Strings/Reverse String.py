class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2): s[i],s[-i-1]=s[-i-1],s[i]
            
            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s1 = list(s)
        s.reverse()
        return ''.join(s1)