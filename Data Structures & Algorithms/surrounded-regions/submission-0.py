class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "*"
            for dx,dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r+dx, c+dy)

        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)
        
        for r in range(1, ROWS-1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS-1] == "O":
                dfs(r, COLS-1)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "*":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"


        