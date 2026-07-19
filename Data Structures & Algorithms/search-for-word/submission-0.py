class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or board[r][c] == "*":
                return False
            board[r][c] = "*"
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ans = dfs(r+d[0], c+d[1], i+1)
                if ans:
                    break
            board[r][c] = word[i]
            return ans
        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, 0)
                if res:
                    return True
        return False
            
                
                


            
            

        