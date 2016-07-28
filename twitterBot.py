import tweepy

auth = tweepy.OAuthHandler("xXxXxXxXxXxXxXxXxXxXxXxXx", "xXxXxXxXxXxXxXxXxXxXxXxXxxXxXxXxXxXxXxXxXxXxXxXxXx")
auth.set_access_token("xXxXxXxXxXxXxXxXxX-xXxXxXxXxXxXxXxXxXxXxXxXxxXxXxX", "xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx")
api = tweepy.API(auth)

results = api.trends_place(23424934)

print("PH Trends")

def getTrend():
    x = 0
    n = ""
    for location in results:
        for trend in location["trends"]:
            if x < 10:
                print (" %s" % trend ["name"])
                n += str(x+1) +". " + trend ["name"] + "\n"
                x = x+1
    return n
