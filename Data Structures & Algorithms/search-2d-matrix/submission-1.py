class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][n-1] < target and l < m-1:
                l = mid + 1
            else:
                r = mid - 1
        row = l
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False