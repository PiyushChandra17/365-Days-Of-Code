class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        list = []
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            b = a + k
            
            if b in nums and nums.index(b)!=i:
                list.append((a,b))
        return len(set(list))
        