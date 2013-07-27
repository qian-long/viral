import tweepy

auth = tweepy.OAuthHandler("key", "key2")

auth.set_access_token("key", "key2")
api = tweepy.API(auth)

tweets = api.search('asiana')

for tweet in tweets:
    print tweet.text


print api.me().name
statuses = api.user_timeline()
for status in statuses:
    print status.text
friends_statuses = api.home_timeline()
for status in friends_statuses:
    print status.text + "\n"
print "My ID is " + api.me().screen_name

myFriends = api.followers_ids('harinidkannan')
for friend in myFriends:
    print "Hellow, my ID is " + str(friend)
    print api.get_user(friend).screen_name


