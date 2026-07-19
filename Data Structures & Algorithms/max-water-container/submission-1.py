class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        ans = 0
        while i < j:
            l = heights[i]
            r = heights[j]
            ans = max(ans, (j-i)*min(l, r))
            if l < r:
                i+=1
            else:
                j -= 1
        return ans
        