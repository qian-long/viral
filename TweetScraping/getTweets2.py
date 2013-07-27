import tweepy
import json
import calendar
auth = tweepy.OAuthHandler("t1JGNM84dllz91Jk8BhkQ", "Mut0O8YZGmUh1XyjL890NHUAGhngEOtNNyhFn9dzus")

auth.set_access_token("1467714804-R7au6WYyiyUn6yIBZuOa8Ld1hVVUwfpe7hVLhHy", "gDBEcZVmmpMlIKDhPVOo7T0r1N01qyCzujnb6BypGQ")
api = tweepy.API(auth)

#tweets = api.search('', count=1000)
counter = 0
output = []
#print len(tweets)
current_id = 360973835627020288
while counter < 10000:
    tweets = api.search('royal baby', count=100, result_type='recent', max_id = current_id)
    for tweet in tweets:
        dict = {}
        counter = counter + 1
#       print str(counter) + tweet.text + str(tweet.created_at)
        if tweet.coordinates is not None:
            dict["lat"] = tweet.coordinates['coordinates'][1]
            dict["long"] = tweet.coordinates['coordinates'][0]
            dict["ID"] = tweet.id
            dict["text"] = tweet.text
            timestamp = calendar.timegm(tweet.created_at.utctimetuple())
            dict["time"] = timestamp
            output.append(dict)
        elif tweet.geo is not None:
            dict["lat"] = tweet.geo['coordinates'][0]
            dict["long"] = tweet.geo['coordinates'][1]
            dict["ID"] = tweet.id
            dict["text"] = tweet.text
            timestamp = calendar.timegm(tweet.created_at.utctimetuple())
            dict["time"] = timestamp
            output.append(dict)
    current_id = tweets.since_id

answer = json.dumps(output)
print answer
print "//" + str(current_id)

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

