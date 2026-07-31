class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        l = 0
        r = len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid - 1

        intervals.insert(l, newInterval)
            
        
        for j in range(len(intervals)):
            a,b = intervals[j]
            if len(ans) == 0:
                ans.append([a, b])
            elif ans[-1][0] <= a <= ans[-1][1]:
                al, bl = ans.pop()
                ans.append([al, max(bl, b)])
            else:
                ans.append([a,b])
        return ans

            
                
