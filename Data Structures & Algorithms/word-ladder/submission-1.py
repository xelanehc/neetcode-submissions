class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (beginWord == endWord) or (endWord not in wordList):
            return 0
        
        q = deque()
        q.append(beginWord)
        words = set(wordList)
        res = 0

        while q:
            res += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    for c in range(97, 123):
                        if chr(c) == cur[j]:
                            continue
                        nei = cur[:j] + chr(c) + cur[j + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0
                        
