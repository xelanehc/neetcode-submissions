class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = defaultdict(set)
        vertical = defaultdict(set)
        square = defaultdict(set)
        vboard = [[""] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                box = board[i][j]
                vboard[j][i] = box
                if box == ".":
                    continue
                if box in horizontal[i]:
                    return False
                else:
                    horizontal[i].add(box)
        for i in range(9):
            for j in range(9):
                box = vboard[i][j]
                if box == ".":
                    continue
                if box in vertical[i]:
                    return False
                else:
                    vertical[i].add(box)
        for n in range(3):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        box = board[n*3 + j][i*3 + k]
                        if box == ".":
                            continue
                        if box in square[i + n*3]:
                            return False
                        else:
                            square[i + n*3].add(box)
        return True
