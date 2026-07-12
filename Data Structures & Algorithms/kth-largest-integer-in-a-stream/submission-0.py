import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.arr = nums
       self.arr.sort()
       self.k = k 

    def add(self, val: int) -> int:
        bisect.insort(self.arr, val)
        return self.arr[-self.k]

