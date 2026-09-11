class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res, wordList = 0, set(wordList)
        q = deque([beginWord])

        while q:
            lenq = len(q)
            res += 1
            for i in range(lenq):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for c in range(len(cur)):
                    for j in range(ord('a'), ord('a') + 26):
                        if chr(j) == cur[c]:
                            continue
                        temp = cur[:c] + chr(j) + cur[c + 1:]
                        if temp in wordList:
                            q.append(temp)
                            wordList.remove(temp)
        return 0