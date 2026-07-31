class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        ap, bp = newInterval
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
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

            
                
