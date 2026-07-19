class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        l, r = 0, nrows*ncols - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // ncols
            col = mid % ncols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            

        