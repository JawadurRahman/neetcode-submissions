class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hashs = {}
        for i, n in enumerate(nums):
            if target - n in hashs:
                return [hashs[target - n], i]
            hashs[n] = i
        return []
