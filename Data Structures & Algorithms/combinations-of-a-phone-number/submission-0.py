class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {"2": "abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8": "tuv",
                    "9":"wxyz"}
        ans = []
        if not digits:
            return ans
        def dfs(i, path):
            if i == len(digits):
                ans.append(path)
                return
            choices = letterMap[digits[i]]
            for c in choices:
                path += c
                dfs(i+1, path)
                path = path[:-1]
        dfs(0, "")
        return ans

        