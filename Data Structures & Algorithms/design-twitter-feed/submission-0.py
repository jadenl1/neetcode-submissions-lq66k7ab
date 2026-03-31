import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> list[(time, tweetId)]
        self.follows = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # Decreasing ensures newest = smallest for min-heap
        self.follows[userId].add(userId)  # Ensure user follows self

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        for followeeId in self.follows[userId]:
            for tweet in self.tweets[followeeId][-10:]:  # only need last 10 tweets per user
                heapq.heappush(heap, tweet)
        return [tweetId for (_, tweetId) in heapq.nsmallest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        self.follows[followerId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
