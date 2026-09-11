class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (beginWord == endWord) or (endWord not in wordList):
            return 0
        words = set(wordList)
        q = deque([beginWord])
        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    for k in range(97, 123):
                        if word[j] == chr(k):
                            continue
                        cur = word[:j] + chr(k) + word[j + 1:]
                        if cur in words:
                            q.append(cur)
                            words.remove(cur)
        return 0