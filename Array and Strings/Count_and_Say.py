class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            s = re.sub(r'(.)\1*',lambda m: str(len(m.group(0)))+m.group(1),s)
        return s

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            s = ''.join(str(len(list(group)))+digits for digits,group in itertools.groupby(s))
        return s