class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = len(temperatures) * [0]
        for i, t in enumerate(temperatures):
            if not stack or t <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < t:
                    last = stack.pop()
                    result[last] = i - last
                stack.append(i)
        return result
            

            
        