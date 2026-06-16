class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashset = Counter(nums)
        nums.sort()
        ans = []
        count = defaultdict(int)
        print(nums)
        for i, numi in enumerate(nums):
            hashset[numi] -= 1
            # numj + numk = -numi
            for j in range(i + 1, len(nums)):
                numj = nums[j]
                hashset[numj] -= 1
                numk = -numi - numj
                if hashset[numk] and count[frozenset((numi, numj, numk))] == 0:
                    ans.append([numi, numj, numk])
                    count[frozenset((numi, numj, numk))] += 1
                hashset[numj] += 1
            hashset[numi] += 1
        return ans