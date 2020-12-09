class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'
        stack,num,sign = [],0,"+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign,num = s[i],0
        return sum(stack)