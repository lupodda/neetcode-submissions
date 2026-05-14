from collections import defaultdict, deque
import heapq
class Twitter:

    def __init__(self):
        # dict with usr_id:queue for the feed with capacity of 10
        # dict with usr_id:set for folloed people
        # dict with usr_id:set for following people
        self.feed_capacity = 10
        self.index = 0 
        # self.feeds = defaultdict(list)
        self.posted_tweets = defaultdict(list)
        self.followed_by = defaultdict(set)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posted_tweets[userId].append((self.index,tweetId))
        self.index += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following_users = self.followers[userId]
        users = following_users
        users.add(userId)
        heap = []
        for user in following_users:
            posted_tweets = self.posted_tweets[user]
            for post in posted_tweets:
                heapq.heappush(heap, post)
                if len(heap) > self.feed_capacity:
                    heapq.heappop(heap)

        heap.sort(key=lambda item: item[0], reverse=True)
        return [tweetId for index, tweetId in heap]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


