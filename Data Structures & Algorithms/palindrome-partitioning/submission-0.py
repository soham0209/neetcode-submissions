class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.is_pali(i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def is_pali(self, l, r):
        while l < r:
            if self.s[l] != self.s[r]:
                return False
            l += 1
            r -= 1
        return True
            
    
        