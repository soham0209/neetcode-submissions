class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, ht = stack.pop()
                maxArea = max(maxArea, ht*(i - start))
            stack.append((start, h))
        for start, h in stack:
            maxArea = max(maxArea, h*(len(heights) - start))
        return maxArea

        