class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) == 0:
            return True
        row_map = {}
        col_map = {}
        grid_map = {}
        for row in range(len(board)):
            row_map[row] = set()
            for col in range(len(board[0])):
                if col not in col_map:
                    col_map[col] = set()
                grid_num = (row // 3) * 3 + (col // 3)
                if grid_num not in grid_map:
                    grid_map[grid_num] = set()
                num = board[row][col]
                if num == ".":
                    continue
                num = int(num)
                if num in row_map[row] or num in col_map[col] or num in grid_map[grid_num]:
                    return False
                print(f"num={num} row={row} col={col} grid={grid_num}")
                row_map[row].add(num)
                col_map[col].add(num)
                grid_map[grid_num].add(num)
        return True
        