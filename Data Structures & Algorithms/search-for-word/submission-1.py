class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROW, COL = len(board), len(board[0])

        def search(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            
            found = (search(row + 1, col, index + 1)
                or search(row - 1, col, index + 1)
                or search(row, col + 1, index + 1)
                or search(row, col - 1, index + 1))
            
            visited.remove((row, col))

            return found

        for row in range(ROW):
            for col in range(COL):
                if search(row, col, 0):
                    return True
        
        return False