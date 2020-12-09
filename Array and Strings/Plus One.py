class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = reduce(lambda x,y:x*10+y,digits)+1
        return [int(i) for i in str(num)]