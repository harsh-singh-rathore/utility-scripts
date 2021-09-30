import tweepy
from dotenv import load_dotenv
load_dotenv()


api = tweepy.API(auth)
# these are the tweets visible in home
public_tweets = api.home_timeline()
user = api.get_user('sarthakgyahun')
print(user.followers_count)
print(user.screen_name)
print(api.friends)
# for friend in tweepy.Cursor(api.friends).items():
#     print(friend)
# for tweet in public_tweets:
#     print(tweet.)

api.update_status('Lmaooooo')