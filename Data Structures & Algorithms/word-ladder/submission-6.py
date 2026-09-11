class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        q = deque([beginWord])
        words = set(wordList)

        while q:
            lenQ = len(q)
            res += 1
            for i in range(lenQ):
                cur = q.popleft()
                if cur == endWord:
                    return res
                
                for c in range(len(cur)):
                    for j in range(ord('a'), ord('a') + 26):
                        if chr(j) == cur[c]:
                            continue
                        newWord = cur[:c] + chr(j) + cur[c + 1:]
                        if newWord in words:
                            q.append(newWord)
                            words.remove(newWord)
        
        return 0