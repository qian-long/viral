import tweepy
import json
import calendar
auth = tweepy.OAuthHandler("fmOVYZLqm0uSBkCS1tLCQ", "G94sqrzpCgcy7ZUEZxv5j8IMjgKG3gpVCpI4PqdH8")

auth.set_access_token("1467714804-Xjbb3fuTT6abBj6QIQasyVnJSJo7XXvkI6Rz9Yr", "c2lD0qQZQku99fdBDpRmVGyn0NVEVVkNq4tSNLvI59s")
api = tweepy.API(auth)

#tweets = api.search('', count=1000)
counter = 0
output = []
#print len(tweets)
current_id = 360973835627020288
while counter < 31:
    tweets = api.search('royal baby', count=15, result_type='recent', max_id = current_id)
    for tweet in tweets:
        dict = {}
        counter = counter + 1
#       print str(counter) + tweet.text + str(tweet.created_at)
        #dict["lat"] = None
        #dict["long"] = None
        #dict["loc"] = None
        if tweet.coordinates is not None:
            dict["lat"] = tweet.coordinates['coordinates'][1]
            dict["long"] = tweet.coordinates['coordinates'][0]
        elif tweet.geo is not None:
            dict["lat"] = tweet.geo['coordinates'][0]
            dict["long"] = tweet.geo['coordinates'][1]
'''
        else:
            dict["lat"] = None
            dict["long"] = None
            if tweet.user.location is not None:
                dict["loc"] = tweet.user.location                
'''
        dict["ID"] = tweet.id
        dict["text"] = tweet.text
        timestamp = calendar.timegm(tweet.created_at.utctimetuple())
        dict["time"] = timestamp
        output.append(dict)
    current_id = tweets.since_id

print output
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

