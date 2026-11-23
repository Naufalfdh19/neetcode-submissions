class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(dict)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        dirtyTweets = []

        for followeeId in self.followers[userId]:
            for time, tweet in self.tweets[followeeId]:
                dirtyTweets.append((-time,tweet))
        
        for time, tweet in self.tweets[userId]:
            dirtyTweets.append((-time,tweet))
        
        heapq.heapify(dirtyTweets)
        
        cleanTweets = []
        count = 0
        while dirtyTweets and count < 10:
            _, tweet = heapq.heappop(dirtyTweets)
            cleanTweets.append(tweet)
            count += 1

        return cleanTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            del self.followers[followerId][followeeId]
