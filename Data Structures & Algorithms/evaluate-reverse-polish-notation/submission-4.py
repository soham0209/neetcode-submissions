class Solution:
    def calculate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return int(float(a)/b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '*', '-', '/'])
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            elif t in ops:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                x = self.calculate(a, b, t)
                stack.append(x)
        return stack[-1]
            
        