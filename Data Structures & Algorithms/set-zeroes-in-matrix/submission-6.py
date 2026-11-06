class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        r0 = set()
        c0 = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    r0.add(r)
                    c0.add(c)
        
        for r in r0:
            for i in range(COLS):
                matrix[r][i] = 0

        for c in c0:
            for i in range(ROWS):
                matrix[i][c] = 0
        