import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        heapq.heappush(self.tweets[userId], (self.tweetCount, tweetId))
        self.tweetCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = []

        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                feeds.append(tweet)
            
        if userId in self.followers:
            for follower in self.followers[userId]:
                for tweet in self.tweets[follower]:
                    feeds.append(tweet)

        feeds = sorted(feeds, key=lambda x:x[0], reverse=True)
        
        return [feeds[idx][1] for idx in range(min(len(feeds), 10))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {}
        if followerId != followeeId:
            self.followers[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            del self.followers[followerId][followeeId]
