import tweepy

auth = tweepy.OAuthHandler("KDTmC5RtLO9qBe4nIQUfRdrfe", "noEGv9jWJjvdSz9nY55Y9u5F4ForzxbVEUjH5UlMymQT2WlQRc")
auth.set_access_token("757746084298919936-k4BgOiQqrYa5hUWegwf0VcNuaB5ScZh", "ijy3OQOXKcf0rZZUpYRTxZHonRb2el1YvgtTK2SxortZU")
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