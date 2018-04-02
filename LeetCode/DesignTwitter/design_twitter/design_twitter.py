import datetime

class User(object):

    def __init__(self, id):
        self.id = id
        self.following = set()
        self.following.add(id)

    def follow(self, id):
        self.following.add(id)

    def unfollow(self, id):
        if id != self.id and id in self.following:
            self.following.remove(id)

    def getFollowing(self):
        return self.following

class Tweet(object):

    def __init__(self, id, userId):
        self.id = id
        self.userId = userId
        self.postedOn = datetime.datetime.now().timestamp()

    def getUser(self):
        return self.userId

class Twitter(object):

    def __init__(self):
        self.users = dict()
        self.tweets = dict()

    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.tweets[tweetId] = Tweet(tweetId, userId)

    def getNewsFeed(self, userId):
        if userId not in self.users:
            return []
        user = self.users[userId]
        following = user.getFollowing()
        tweets = list()
        for tweetId in self.tweets:
            if self.tweets[tweetId].getUser() in following:
                tweets.append(self.tweets[tweetId])
        tweets.sort(key=lambda x: x.postedOn, reverse=True)
        tweetIdList = list()
        for tweet in tweets:
            tweetIdList.append(tweet.id)
        return tweetIdList[:10]

    def follow(self, followerId, followeeId):
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId not in self.users or followeeId not in self.users:
            return
        self.users[followerId].unfollow(followeeId)


from nose.tools import assert_equals, assert_raises

class TestTwitter(object):

  def testTwitter(self):
    twitter = Twitter()

    twitter.postTweet(1, 5);

    assert_equals(twitter.getNewsFeed(1), [5]);

    twitter.follow(1, 2);

    twitter.postTweet(2, 6);

    assert_equals(twitter.getNewsFeed(1), [6,5]);

    twitter.unfollow(1, 2);

    assert_equals(twitter.getNewsFeed(1), [5]);

    print ("All test cases passed!")


def main():
  testTwitter = TestTwitter()
  testTwitter.testTwitter()

if __name__ == '__main__':
  main()
