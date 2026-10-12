class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord == beginWord) or (endWord not in wordList):
            return 0
        
        words = set(wordList)
        q = deque([beginWord])
        res = 0

        while q:
            res += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    for k in range(97, 123):
                        if chr(k) == cur[j]:
                            continue
                        neighbor = cur[:j] + chr(k) + cur[j + 1:]
                        if neighbor in words:
                            q.append(neighbor)
                            words.remove(neighbor)
        return 0
