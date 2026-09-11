class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tracker = set()
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in tracker:
                        return False
                tracker.add(num)
        for i in range(9):
            tracker = set()
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in tracker:
                        return False
                tracker.add(num)
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                tracker = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row + i][col + j]
                        if num != ".":
                            if num in tracker:
                                return False
                        tracker.add(num)
        return True
