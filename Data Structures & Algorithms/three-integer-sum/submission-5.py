class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        nums.sort()
        ans = []

        for i, numi in enumerate(nums):
            count[numi] -= 1
            if i >= 1 and nums[i] == nums[i - 1]: 
                continue
            
            for j in range(i + 1, len(nums)):
                numj = nums[j]
                count[numj] -= 1

                if j - i > 1 and nums[j] == nums[j - 1]: 
                    continue
                
                numk = -numi - numj
                if count[numk] > 0:
                    ans.append([numi, numj, numk])
                    
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return ans