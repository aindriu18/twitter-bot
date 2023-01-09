from keys import *
import tweepy
import time


auth = tweepy.OAuth1UserHandler(
   api_key,
   api_secret,
   access_token,
   access_token_secret
)

api = tweepy.API(auth)
user = api.verify_credentials()

# creating a helper function to make sure we do not hit API rate limit.

def limit_handler(cursor):
   try:
      while True:
         # cursor is a generator
         yield cursor.next()
   except tweepy.TooManyRequests:
      # Will pause to make sure rate limit is not hit
      time.sleep(1000)
   except StopIteration:
      return


for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
   if follower.name == 'Denise Lao':
      follower.follow()
      break

   