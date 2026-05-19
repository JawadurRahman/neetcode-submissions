class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute
        if len(nums) == 0: return 0
        unique_list = list(set(nums))
        unique_list.sort()
        ans = 1
        temp = 1
        for i in range(len(unique_list) - 1):
            print(unique_list[i], unique_list[i+1])
            if unique_list[i] == unique_list[i+1] - 1:
                temp += 1
            else:
                temp = 1
            ans = max(ans, temp)
        return ans
