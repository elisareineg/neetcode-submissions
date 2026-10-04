import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)  # userId -> [(timestamp, tweetId)]
        self.following = defaultdict(set)     # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1  # decreasing, so the min-heap pops the most recent first

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        for author_id in self.following[userId] | {userId}:
            tweets = self.user_tweets[author_id]
            if tweets:
                newest_index = len(tweets) - 1
                timestamp, tweet_id = tweets[newest_index]
                heap.append((timestamp, tweet_id, author_id, newest_index - 1))
        heapq.heapify(heap)

        while heap and len(feed) < 10:
            timestamp, tweet_id, author_id, next_older_index = heapq.heappop(heap)
            feed.append(tweet_id)
            if next_older_index >= 0:
                older_timestamp, older_tweet_id = self.user_tweets[author_id][next_older_index]
                heapq.heappush(heap, (older_timestamp, older_tweet_id, author_id, next_older_index - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
