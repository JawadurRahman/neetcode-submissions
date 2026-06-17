class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # (r - l) * min(heights[r], heights[l])
        l = 0
        maxA = 0
        r = len(heights) - 1
        while l < r:
            maxA = max(maxA, (r - l) * min(heights[r], heights[l]))
            if heights[r] >= heights[l]: l += 1
            else: r -= 1
        return maxA
