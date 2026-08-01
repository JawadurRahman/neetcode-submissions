class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = []
        for a,b in intervals:
            if ans and ans[-1][1] > a:
                if ans[-1][1] > b:
                    ans[-1] = [a, b]
                continue
            else:
                ans.append([a, b])
        return len(intervals) - len(ans)