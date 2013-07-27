import tweepy
import json
import calendar
auth = tweepy.OAuthHandler("MTS6yOt6FMiPO9901Nzeg", "O92CIx5F11bwqmVj6unLLv4jvzwqe3E8eAPXCjAPlM")

auth.set_access_token("45437141-GlEEbvfpgzy3jK5PexejHux3nVKR9J7Ra0DKoEFn9", "u98Oe57ibDoWEuoaCAgCtenFljspgaOnest2TXoExZU")
api = tweepy.API(auth)

#tweets = api.search('', count=1000)
counter = 0
output = []
#print len(tweets)
current_id = 360973835627020288
while counter < 30:
    tweets = api.search('royal baby', count=15, result_type='recent', max_id = current_id)
    for tweet in tweets:
        dict = {}
        counter = counter + 1
#       print str(counter) + tweet.text + str(tweet.created_at)
        dict["loc"] = None
        if (tweet.coordinates is not None):
            dict["lat"] = tweet.coordinates[1]
            dict["long"] = tweet.coordinates[0]
        elif (tweet.geo is not None):
            dict["lat"] = tweet.geo[0]
            dict["long"] = tweet.geo[1]
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

print output

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

