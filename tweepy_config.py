import tweepy

ckey=''
csecret=''
atoken=''
asecret=''
auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api=tweepy.API(auth)