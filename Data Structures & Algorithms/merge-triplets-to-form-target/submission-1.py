class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        start = [0,0,0]

        for x,y,z in triplets:
            if max(start[0], x) <= target[0] \
                and max(start[1], y) <= target[1] \
                and max(start[2], z) <= target[2]:
                start[0] = max(start[0], x)
                start[1] = max(start[1], y)
                start[2] = max(start[2], z)

            print(start)

        return start == target