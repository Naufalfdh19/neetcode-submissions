class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(dict)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        dirtyTweets = []

        for followeeId in self.followers[userId]:
            tweets = self.tweets[followeeId]

            if tweets:
                idx = len(tweets)-1
                mTime, tweetId = tweets[idx]
                dirtyTweets.append((mTime,tweetId,followeeId,idx))

        tweets = self.tweets[userId]
        if tweets:
            idx = len(tweets)-1
            mTime, tweetId = tweets[idx]
            dirtyTweets.append((mTime,tweetId,userId,idx))
        
        heapq.heapify(dirtyTweets)
        
        cleanTweets = []
        count = 0
        while dirtyTweets and count < 10:
            _, tweetId, followeeId,idx = heapq.heappop(dirtyTweets)
            cleanTweets.append(tweetId)

            mTime, newTweetId = 0, 0
            if idx-1 >= 0:
                mTime, newTweetId = self.tweets[followeeId][idx-1]
                heapq.heappush(dirtyTweets, (mTime,newTweetId,followeeId,idx-1))

            count += 1

        return cleanTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            del self.followers[followerId][followeeId]
