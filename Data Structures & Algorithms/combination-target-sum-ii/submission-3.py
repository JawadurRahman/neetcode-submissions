class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        candidates.sort()
        def dfs(index, sum):
            if sum == target:
                ans.append(temp.copy())
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue                    
                num = candidates[i]
                if sum + num > target:
                    break;
                temp.append(num)
                dfs(i + 1, sum + num)
                temp.pop()
        dfs(0, 0)
        return ans
