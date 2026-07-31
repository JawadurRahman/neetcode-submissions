class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        ap, bp = newInterval
        i = 0
        if not intervals: ans.append(newInterval)
        for a,b in intervals:
            i += 1
            if ap < a:
                if bp < a:
                    ans.append(newInterval)
                    ans.append([a,b])
                else:
                    ans.append([min(a, ap), max(b,bp)])
                break
            elif a <= ap <= b:
                ans.append([min(a, ap), max(b,bp)])
                break
            else:
                ans.append([a,b])

            if i == len(intervals): ans.append(newInterval)
        
        for j in range(i, len(intervals)):
            a,b = intervals[j]
            if ans[-1][0] <= a <= ans[-1][1]:
                al, bl = ans.pop()
                ans.append([al, max(bl, b)])
            else:
                ans.append([a,b])
        return ans

            
                
