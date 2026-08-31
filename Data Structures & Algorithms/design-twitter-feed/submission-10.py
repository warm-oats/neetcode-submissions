class Twitter:
    def __init__(self):
        self.tweets_map = defaultdict(list)
        self.user_follows_map = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users_followed = [userId] + self.user_follows_map[userId]
        temp = []
        res = []

        for followeeId in users_followed:
            for tweet in self.tweets_map[followeeId]:
                heapq.heappush(temp, tweet)

        while temp and len(res) < 10:
            res.append(heapq.heappop(temp)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        follow_map = self.user_follows_map[followerId]

        if followerId != followeeId and followeeId not in follow_map:
            self.user_follows_map[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower_arr = self.user_follows_map[followerId]

        if followerId == followeeId:
            return

        for i in range(len(follower_arr)):
            if follower_arr[i] == followeeId:
                self.user_follows_map[followerId] = follower_arr[:i] + follower_arr[i+1:]
                break