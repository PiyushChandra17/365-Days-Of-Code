class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        
        regex = re.findall('^[\+\-]?0*\d+',s.strip())
        if regex:
            num = int(regex[0])
            if num > MAX_INT:
                return MAX_INT
            elif num < MIN_INT:
                return MIN_INT
            else:
                return num
        else:
            return 0