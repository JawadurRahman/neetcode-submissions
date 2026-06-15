from _bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            idx = bisect_left(numbers, target - n)
            if idx < len(numbers) and numbers[idx] == target - n:
                return [i + 1, idx + 1]

        return []