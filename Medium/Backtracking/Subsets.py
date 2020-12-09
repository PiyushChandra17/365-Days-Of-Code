class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda L,ele: L+[l+[ele] for l in L],nums,[[]])

#OR

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res