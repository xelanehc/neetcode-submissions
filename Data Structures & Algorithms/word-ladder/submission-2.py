class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        queue = deque([beginWord])
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    for k in range(97, 123):
                        if chr(k) == word[j]:
                            continue
                        newWord = word[:j] + chr(k) + word[j + 1:]
                        if newWord in words:
                            queue.append(newWord)
                            words.remove(newWord)
        return 0