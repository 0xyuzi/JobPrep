class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # mirror in horizental 
        N = len(matrix)
        
        for i in range(N//2):
            for j in range(N):
                matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]
        
        # swap the diagnoal from top to bottom 
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        return matrix