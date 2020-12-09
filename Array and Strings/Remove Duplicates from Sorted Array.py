class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = OrderedDict.fromkeys(nums).keys()
        return len(nums)

#or

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

