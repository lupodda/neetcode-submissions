from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.capacity = 10
        self.followees = defaultdict(set)
        self.posted_tweets = defaultdict(list)
        self.index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.index += 1
        self.posted_tweets[userId].append((self.index, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followees[userId]
        followees.add(userId)
        heap = []
        res =[]

        for followee in followees:
            posted_tweets = self.posted_tweets[followee]
            if posted_tweets:
                index = len(posted_tweets)-1 # index is the index of the next most recent tweet for that user
                heapq.heappush_max(heap, (posted_tweets[index], followee, index-1))

        while heap and len(res) < 10:                
            latest_tweet, followee, index = heapq.heappop_max(heap)
            res.append(latest_tweet[1])

            if index >= 0:  
                heapq.heappush_max(heap, (self.posted_tweets[followee][index], followee, index-1))

        return res

            # for index,tweet in posted_tweets:
            #     heapq.heappush(heap, (index,tweet))
            #     if len(heap)>self.capacity:
            #         heapq.heappop(heap)

        # heap = sorted(heap, reverse = True) # or heap.sort(key=lambda item: item[0], reverse = True)
        #                                     # for the second key- > heap.sort(key=lambda item:item[1], reverse = True)
        # return [tweet for _, tweet in heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId) # or use discard

