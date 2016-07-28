import twitterBot
import schedule
import time
from slackclient import SlackClient

BOT_ID = "XXXXXXXXX"

slack_client = SlackClient('xxxx-NNNNNNNNNNN-XXXxxxxxxxxxxxXXXXXXXXXX')

tweetIt = twitterBot.getTrend()

def post_message():
    slack_client.api_call("chat.postMessage", channel="tweetbot", text="Top 10 Trends in PH \n" + tweetIt, as_user=True)
    slack_client.api_call("chat.postMessage", channel="python_practice1", text="Top 10 Trends in PH \n" + tweetIt, as_user=True)

if __name__ == "__main__":
    schedule.every().day.at("02:00").do(post_message)
    while True:
        schedule.run_pending()
