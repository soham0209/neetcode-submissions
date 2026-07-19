class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        nrows, ncols = len(matrix), len(matrix[0])
        firstRow = False
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        firstRow = True
        
        for i in range(1, nrows):
            for j in range(1, ncols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for r in range(nrows):
                matrix[r][0] = 0
        if firstRow:
            for c in range(ncols):
                matrix[0][c] = 0
        
        