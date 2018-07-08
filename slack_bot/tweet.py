import sys, os
import twitter


class Tweet(object):
    consumer_key = ""
    consumer_secret = ""
    access_token_key = ""
    access_token_secret = ""

    def __init__(self):
        # set keys as vars from env vars
        self.consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        self.consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        self.access_token_key = os.environ['TWITTER_ACCESS_TOKEN']
        self.access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    def get_session(self):
        sesh = twitter.Api(consumer_key=self.consumer_key,
                            consumer_secret=self.consumer_secret,
                            access_token_key=self.access_token_key,
                            access_token_secret=self.access_token_secret)

        return sesh

    def post_message(handle, message):
        t = Tweet()
        sesh = t.get_session()
        sesh.PostUpdate(handle, message)
