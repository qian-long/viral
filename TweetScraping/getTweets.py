import tweepy

auth = tweepy.OAuthHandler("Dymgnrgon9xzUPiVaLdysw", "NbvrqBFFW9LVAqZ5Jd305EJOB2dNV2JAckYBu3EqB3o")

auth.set_access_token("1467714804-03r0XdOXrq2Xi3OCTiLi4ztjaPzPkYSpq18LlBB", "hmWr6tshZ3TpGt9uEYCX8Wa32TfHSL25onegjjvHg")
api = tweepy.API(auth)

tweets = api.search('asiana', count=1000)
counter = 0
print len(tweets)
for tweet in tweets:
    counter = counter + 1
    print str(counter) + tweet.text + tweet.id

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

