class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        row = -1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][-1] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        row = lo + ((hi - lo) // 2)
        lo, hi = 0, len(matrix[0]) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

