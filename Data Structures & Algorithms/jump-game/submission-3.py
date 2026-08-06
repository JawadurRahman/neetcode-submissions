class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n - 1):
            if i > farthest: return False
            if nums[i] + i > farthest:
                farthest = nums[i] + i

        return farthest >= n - 1