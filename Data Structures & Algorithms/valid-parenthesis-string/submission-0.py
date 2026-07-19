class Solution:
    def checkValidString(self, s: str) -> bool:
        lstack, sstack = [], []
        for i, c in enumerate(s):
            if c == '(':
                lstack.append(i)
            elif c == '*':
                sstack.append(i)
            else:
                if not lstack and not sstack:
                    return False
                if lstack:
                    lstack.pop()
                else:
                    sstack.pop()
        while lstack and sstack:
            if lstack.pop() > sstack.pop():
                return False
        return not lstack
        

        