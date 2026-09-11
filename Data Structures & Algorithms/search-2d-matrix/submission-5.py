class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = -1
        while l < r:
            row = l + (r - l) // 2
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                break
            elif matrix[row][-1] > target:
                r = row - 1
            else:
                l = row + 1
        
        row = l + (r - l) // 2
        l, r = 0, len(matrix[0]) - 1
        
        while l <= r:
            col = l + (r - l) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = col - 1
            else:
                l = col + 1
        
        return False