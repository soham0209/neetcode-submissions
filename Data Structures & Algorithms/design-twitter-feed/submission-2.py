class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        users = [(1, userId)]+[(1, user) for user in self.followMap[userId]]
        while users:
            idx, user = users.pop(0)
            tweets = self.tweetMap[user]
            if len(tweets) <  idx:
                continue
            time, tweetid = tweets[-idx]
            heapq.heappush(h, (time, tweetid))
            if len(h) > 10:
                heapq.heappop(h)
            idx += 1
            users.append((idx, user))
        ans = [heapq.heappop(h)[1] for i in range(len(h))]
        res = [ans[i] for i in range(len(ans)-1, -1, -1)]
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
