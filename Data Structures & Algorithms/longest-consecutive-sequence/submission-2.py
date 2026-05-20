class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute
        if len(nums) == 0: return 0
        hashset = set(nums)
        seen = set()
        unique_list = list(set(nums))
        unique_list.sort()
        
        ans = 1
        temp = 1
        for n in hashset:
            if n in seen: continue
            seen.add(n)
            n2 = n
            while n + 1 in hashset:
                temp += 1
                seen.add(n + 1)
                n = n + 1
            while n2 - 1 in hashset:
                temp += 1
                seen.add(n2 - 1)
                n2 = n2 - 1
            ans = max(ans, temp)
            temp = 1
        return ans
