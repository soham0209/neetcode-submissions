class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stk.append(c)
            elif c == ")":
                if stk and stk[-1] == "(":
                    stk.pop(-1)
                else:
                    return False
            elif c == "}":
                if stk and stk[-1] == "{":
                    stk.pop(-1)
                else:
                    return False
            elif c == "]":
                if stk and stk[-1] == "[":
                    stk.pop(-1)
                else:
                    return False
        return len(stk) == 0
            

        