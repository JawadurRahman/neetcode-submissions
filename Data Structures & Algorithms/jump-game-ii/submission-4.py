class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        n = len(nums)
        if n == 1: return 0
        count = 0
        l = 0
        r = nums[l]
        while r < n - 1:
            newl = r
            for i in range(l, r + 1):
                if i + nums[i] > farthest:
                    farthest = i + nums[i]
                    newl = i
            l = newl
            r = farthest
            count += 1

        return count + 1