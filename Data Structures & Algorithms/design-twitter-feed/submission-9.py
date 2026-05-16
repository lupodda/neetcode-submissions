from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count+=1        

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followees[userId]
        followees.add(userId)
        heap = []
        res = []

        for followee in followees:
            posted_tweets = self.tweets[followee]

            if posted_tweets:
                index = len(posted_tweets)-1
                heapq.heappush_max(heap, (posted_tweets[index], followee, index-1))
        
        while heap and len(res) < 10:
            latest_tweet, followee, index = heapq.heappop_max(heap)
            res.append(latest_tweet[1])

            if index >= 0:
                heapq.heappush_max(heap, (self.tweets[followee][index], followee, index-1))
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

