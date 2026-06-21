class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        last = 0
        maxArea = 0
        indexIndex, heightIndex = 0, 1
        for i, h in enumerate(heights):
            while stack and stack[-1][heightIndex] >= h:
                i_prev, h_prev = stack.pop()
                area = 0
                if stack:
                    i_top, _ = stack[-1]
                    area += h_prev * (i_prev - i_top - 1)
                else:
                    area += h_prev * (i_prev)
                area += h_prev * (i - i_prev)
                maxArea = max(area, maxArea)
            stack.append((i, h))

        while stack:
            i_prev, h_prev = stack.pop()
            area = h_prev * (len(heights) - i_prev)
            if stack:
                i_top, _ = stack[-1]
                area += h_prev * (i_prev - i_top - 1)
            else:
                area += h_prev * (i_prev)
            maxArea = max(area, maxArea)

        return maxArea