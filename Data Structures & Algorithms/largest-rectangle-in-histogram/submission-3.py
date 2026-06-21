class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        total = [0] * n

        # Left to right
        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][0] > h:
                h_prev, i_prev = stack.pop()
                total[i_prev] = h_prev * (i - i_prev)
            stack.append((h, i))

        for h, i in stack:
            total[i] += h * (n - i)

        # Right to left
        stack = []
        for i, h in enumerate(reversed(heights)):
            while stack and stack[-1][0] > h:
                h_prev, i_prev = stack.pop()
                idx = n - i_prev - 1
                total[idx] += h_prev * (i - i_prev - 1)
            stack.append((h, i))

        for h, i in stack:
            idx = n - i - 1
            total[idx] += h * idx

        return max(total)