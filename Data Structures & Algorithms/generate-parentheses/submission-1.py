class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(l, r, n, s):
            if l > n or r > n or r > l:
                return
            if l == n and r == n:
                res.append(s)
                return
            backtrack(l+1, r, n, s+"(")
            backtrack(l, r+1, n, s+")")
            return
        backtrack(0, 0, n, "")
        return res


        