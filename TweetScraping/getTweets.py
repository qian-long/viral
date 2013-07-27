import tweepy
import json
import calendar
auth = tweepy.OAuthHandler("jmOeCnnbDXgFv3kcHUImQ", "LJLSxZrAV4ZoZK1CJgi8wi1l9O8fNEkcs7EqqsVpE")

auth.set_access_token("45437141-zDplAY0sgKx8AbdgEyeKdY7Z1UDyEyZsdd87x5Edc", "nLYzb5JtNYZMr9h3kpJ0Y2UIgU78Qw4SRAPxMVlvo")
api = tweepy.API(auth)

#tweets = api.search('', count=1000)
counter = 0
output = []
#print len(tweets)
current_id = 360405463675834369
# make 10 apps, run script 10 times
# change current_id!!!!!
iteration = 0
while iteration < 200:
  iteration = iteration + 1
  try:
    tweets = api.search('galicia', count=100, result_type='recent', max_id=current_id)
    for tweet in tweets:
        dict = {}
        #counter = counter + 1
        #print str(counter) + tweet.text + str(tweet.created_at)
        dict["lat"] = None
        dict["long"] = None
        dict["loc"] = None
        if tweet.coordinates is not None:
            dict["lat"] = tweet.coordinates['coordinates'][1]
            dict["long"] = tweet.coordinates['coordinates'][0]
        elif tweet.geo is not None:
            dict["lat"] = tweet.geo['coordinates'][0]
            dict["long"] = tweet.geo['coordinates'][1]
        else:
            dict["lat"] = None
            dict["long"] = None
            if tweet.user.location is not None:
                dict["loc"] = tweet.user.location                
        dict["ID"] = tweet.id
        dict["text"] = tweet.text
        timestamp = calendar.timegm(tweet.created_at.utctimetuple())
        dict["time"] = timestamp
        output.append(dict)
    current_id = tweets.since_id
    #answer = json.dumps(output)
  except (tweepy.error.TweepError):
    print "//reached limit"
    break

answer = json.dumps(output)
print answer
print "//current_id:" + str(current_id) + " time: " + str(output[len(output) - 1]["time"]) + ", size: " + str(len(output))

'''
tweets2 = api.search('asiana', count=100, result_type='recent', max_id=360932756148060160)
for tweet in tweets2:
    counter = counter + 1
    print str(counter) + tweet.text + str(tweet.id)
'''
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

