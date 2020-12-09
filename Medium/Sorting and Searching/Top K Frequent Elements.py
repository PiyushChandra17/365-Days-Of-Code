class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums).most_common(k)
        res = [x[0] for x in cnt]   
        return res
        