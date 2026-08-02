class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        for q in queries:
            temp = None
            for start, end in intervals:
                if start <= q <= end:
                    temp = min(temp, end - start + 1) if temp else end - start + 1

            if temp:
                ans.append(temp)
            else:
                ans.append(-1)
        return ans
                    