
class Twitter:

    def __init__(self):
        # userId: []
        self.tweets = defaultdict(list)
        self.currentTime = 0
        # userId: {}
        self.follow_map = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.currentTime -= 1
        self.tweets[userId].append([self.currentTime,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followingTweets = []
        selfTweets = self.tweets[userId]
        for tweet in selfTweets:
            heapq.heappush(followingTweets,tweet)
        for user in self.follow_map[userId]:
            for tweet in self.tweets[user]:
                heapq.heappush(followingTweets,tweet)
        return [heapq.heappop(followingTweets)[1] for _ in range(min(10, len(followingTweets)))]
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
