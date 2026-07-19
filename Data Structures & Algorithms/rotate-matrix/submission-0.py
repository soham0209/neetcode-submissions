class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        nrow = len(matrix)
        for i in range(nrow//2):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[nrow-1-i][j] = matrix[nrow-1-i][j], matrix[i][j]
        
        for i in range(nrow):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        