class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        visit, res = set(), set()

        def dfs(r, c, node, w):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            w += board[r][c]
            if node.isWord:
                res.add(w)
            dfs(r + 1, c, node, w)
            dfs(r - 1, c, node, w)
            dfs(r, c + 1, node, w)
            dfs(r, c - 1, node, w)

            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, w):
        cur = self
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True