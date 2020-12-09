class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        A[:] = map(list,zip(*A[::-1]))
        
        
class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        A[:] = zip(*A[::-1])
        
class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
        

class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j],A[j][i] = A[j][i],A[i][j]