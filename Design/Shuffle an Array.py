class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.nums
        
        

    def shuffle(self) -> List[int]:
        ans = self.nums[:]
        for i in range(len(ans)-1,0,-1):
            j = random.randint(0,i)
            ans[i],ans[j] = ans[j],ans[i]
        return ans