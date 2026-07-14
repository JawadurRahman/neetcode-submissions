class Twitter:

    def __init__(self):
        self.userToTweet = defaultdict(list)
        self.followToFollowers = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToTweet[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        for followee in self.followToFollowers[userId]:
            for count, tweetId in self.userToTweet[followee]:
                heapq.heappush(ans, (count, tweetId))
        for tweetId in self.userToTweet[userId]:
            heapq.heappush(ans, tweetId)

        return [tid for c, tid in heapq.nsmallest(10, ans)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followToFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followToFollowers[followerId].discard(followeeId)
