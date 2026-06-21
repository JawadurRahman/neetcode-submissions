class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        total = [0]*len(heights)
        for i, h in enumerate(heights):
            while stack and stack[-1][0] > h:
                hprev, iprev = stack.pop()
                total[iprev] = hprev * (i - iprev)
            stack.append((h, i))
            
        for h, i in stack:
            total[i] += h*(len(heights) - i)  

        stack = []
        for i, h in enumerate(reversed(heights)):
            while stack and stack[-1][0] > h:
                hprev, iprev = stack.pop()
                total[len(heights) - iprev - 1] += hprev * (i - iprev - 1)
            stack.append((h, i))
        
        for h, i in stack:
            total[len(heights) -  i - 1] += h*(len(heights) -  i - 1)
            
        return max(total)