class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = []
        for a,b in reversed(intervals):
            if ans and ans[-1][0] < b:
                continue
            else:
                ans.append([a, b])
        return len(intervals) - len(ans)