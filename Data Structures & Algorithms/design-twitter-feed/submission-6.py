from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.tweet = defaultdict(list)
        self.index = 0 
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.index, tweetId))
        self.index += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followees[userId]
        followees.add(userId)
        heap = []
        res = []

        for followee in followees:
            # take the latest tweet for each user
            # push it in max_haep index, userid, list_index-1
            # get the latest absolute tweet
            # push in the heap the next tweet of the latest tweet form the user
            posted_tweets = self.tweet[followee]
            if posted_tweets:
                index = len(posted_tweets)-1
                heapq.heappush_max(heap, (posted_tweets[index], followee, index-1))
        
        while heap and len(res) < 10:
            latest_tweet, followee, index = heapq.heappop_max(heap)
            res.append(latest_tweet[1])
        
            if index >= 0:
                heapq.heappush_max(heap, (self.tweet[followee][index], followee, index-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

        
