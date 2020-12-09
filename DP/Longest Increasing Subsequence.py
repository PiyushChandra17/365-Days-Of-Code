class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            i = bisect.bisect_left(a,num)
            if i == len(a):
                a.append(num)
            else:
                a[i] = num
        return len(a)