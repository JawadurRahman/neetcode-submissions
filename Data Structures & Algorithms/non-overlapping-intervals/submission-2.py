class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = deque([])
        print(intervals)
        for a,b in reversed(intervals):
            if ans and ans[-1][0] < b:
                continue
            else:
                ans.append([a, b])
        print(ans)
        return len(intervals) - len(ans)