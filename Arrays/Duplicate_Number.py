class Solution(object):
    def findDuplicate(self, nums):
        left,right = 0,len(nums)-1
        mid = (right+left)//2
        while right - left > 1:
            count = 0
            for k in nums:
                if mid < k <= right:
                    count += 1
            if count > right - mid:
                left = mid
            else:
                right = mid
            mid = (right+left)//2
        return right
        