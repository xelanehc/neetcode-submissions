class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])

        res = 0
        wordList = set(wordList)

        while q:
            lenQ = len(q)
            res += 1
            for i in range(lenQ):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for c in range(len(cur)):
                    for j in range(26):
                        if chr(j + ord('a')) == cur[c]:
                            continue
                        temp = cur[:c] + chr(j + ord('a')) + cur[c + 1:]
                        if temp in wordList:
                            q.append(temp)
                            wordList.remove(temp)
        return 0
        
        