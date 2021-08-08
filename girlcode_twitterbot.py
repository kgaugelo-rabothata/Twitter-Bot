# Import packages
import pip
import tweepy
import time

# Authenticate to Twitter
consumer_key ='7KoLJoGlM8RYRd3UEvvCjA0MD'
consumer_secret='uzFeKwVSXPX53SgtvYFfPgKkNd1tN1wI9TdJgoW9ESo9WvB7bO'
access_key='1416120438887956485-xN8PzEDppFtz5SXqsJGXSSwYu4dH8Y'
access_secret='DxcDlOXVYFt3OpYfVeeDCkbFjjMWPtAgKvQf3wbgYvued'


# Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit =True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'womenintech'
num_of_tweets = 1000

for  tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:
        
        tweet.retweet()
        print("Retweet")
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break