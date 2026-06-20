class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        prow = None
        while l <= r:
            mid = (l + r)//2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target and target > matrix[mid][len(matrix[0]) - 1]:
                l = mid + 1
            else:
                l = mid + 1
                prow = mid
        if prow is None: return False

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[prow][mid] > target:
                r = mid - 1
            elif matrix[prow][mid] < target:
                l = mid + 1
            else:
                return True
        return False




