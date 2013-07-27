import tweepy
import json

auth = tweepy.OAuthHandler("PyOfxkgs2zbauSJqikg", "lQkKWu7J5KLBLQ8j3lRbHXYtoV0jSb7ZbWcPJJoxQ98")

auth.set_access_token("45437141-ayB9ZSe6yRinekvkhoWFSVjrhcd45HCd9bcTCdNCm", "abgj1mQ5tbEq0YM0TgnGvNGDeDHBhzAlCKIfdx0Y")
api = tweepy.API(auth)

tweets = api.search('asiana', count=100)
counter = 0
"""
print len(tweets)
print tweets[0].created_at
print tweets[0].__getstate__()
print tweets[0].user
print tweets.since_id
print tweets.max_id
"""
output = []
for tweet in tweets:
  if tweet.coordinates != None:
    output.append((tweet.coordinates['coordinates'][1], tweet.coordinates['coordinates'][0]))
  #output.append((tweet.id, tweet.created_at, tweet.coordinates, tweet.geo, tweet.geo[1], tweet.text, tweet.user.location, tweet.user.time_zone, tweet.user.utc_offset))

print output
# pipe this to output file
"""
for tweet in tweets:
    counter = counter + 1
    print str(counter) + tweet.text + tweet.id
"""
'''
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
'''

