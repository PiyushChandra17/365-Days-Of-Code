class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i,n in enumerate(nums):
            while d and nums[d[-1]] <= n:
                d.pop()
            d += [i]
            if i - d[0] >= k:
                d.popleft()
            if i+1 >= k:
                out.append(nums[d[0]])
        return out