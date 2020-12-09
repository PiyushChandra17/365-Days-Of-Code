class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        pi = pj = 1
        for i in range(len(nums)):
            j = -1-i
            
            arr[i] *= pi
            arr[j] *= pj
            pi *= nums[i]
            pj *= nums[j]
        return arr