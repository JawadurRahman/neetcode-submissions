class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dq = deque([(0)])
        aset = set([0])

        while dq:
            for _ in range(len(dq)):
                index = dq.popleft()
                if index == len(nums) - 1: return True
                for dist in range(nums[index] + 1):
                    if dist + index >= len(nums): continue
                    if dist + index in aset: continue
                    if dist == 0: continue
                    dq.append(dist + index)
                    aset.add(dist + index)
        return False