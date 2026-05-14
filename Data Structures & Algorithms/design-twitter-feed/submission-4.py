from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.capacity = 10
        self.followees = defaultdict(set)
        self.followers = defaultdict(set)
        self.posted_tweets = defaultdict(set)
        self.index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.index += 1
        self.posted_tweets[userId].add((self.index, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followees[userId]
        users.add(userId)
        heap = []

        for user in users:
            posted_tweets = self.posted_tweets[user]
            for index,tweet in posted_tweets:
                heapq.heappush(heap, (index,tweet))
                if len(heap)>self.capacity:
                    heapq.heappop(heap)

        heap = sorted(heap, reverse = True)
        return [tweet for _, tweet in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

