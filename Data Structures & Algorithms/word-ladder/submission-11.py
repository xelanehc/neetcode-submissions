class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        res = 0
        words = set(wordList)
        q = deque([beginWord])

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
                        newWord = cur[:j] + chr(c) + cur[j + 1:]
                        if newWord in words:
                            q.append(newWord)
                            words.remove(newWord)
        
        return 0
