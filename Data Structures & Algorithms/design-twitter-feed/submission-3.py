class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweet = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweet, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweet, followeeId, index = heapq.heappop(minHeap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweet, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
