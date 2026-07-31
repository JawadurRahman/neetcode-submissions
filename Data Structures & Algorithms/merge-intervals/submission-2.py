class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i, interval in enumerate(intervals):
            a, b = interval
            if ans and a <= ans[-1][1]:
                ap, bp = ans.pop()
                a = min(a, ap)
                b = max(b, bp)
            ans.append([a,b])
        return ans