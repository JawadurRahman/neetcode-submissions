class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        last = 0
        maxArea = 0
        for h in heights:
            if h > last:
                stack.append([h, 0])
            for i in range(len(stack)):
                stack[i][0] = min(h, stack[i][0])
                stack[i][1] += 1
                maxArea = max(maxArea, stack[i][0] * stack[i][1])
            last = h
        return maxArea