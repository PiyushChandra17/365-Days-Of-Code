class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if "" == digits: return []
        kvmaps = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        return reduce(lambda acc,digit:[x+y for x in acc for y in kvmaps[digit]],digits,[''])


    def letterCombinations(self, digits: str) -> List[str]:
        b = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        return [] if digits=="" else ["".join(x) for x in itertools.product(*(b[d] for d in digits if d in b))]


        def letterCombinations(self, digits: str) -> List[str]:
        
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0: return []
        return [a+b for a in self.letterCombinations(digits[:-1])
                    for b in self.letterCombinations(digits[-1] )] or list(map[digits])

    def letterCombinations(self, digits: str) -> List[str]:
        
      
        if not digits:
            return []
        results = ['']
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        for digit in digits:
            results = [result+d for result in results for d in map[digit]]

        return results