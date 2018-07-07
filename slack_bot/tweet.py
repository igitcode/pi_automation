import sys, os
import twitter


class Tweet(object):

    def __init__(self):
        # run shell script to set keys as env vars
#        os.system('./start.sh')
#        os.system('env')

        # set keys as vars from env vars
        self.consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        self.consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        self.access_token_key = os.environ['TWITTER_ACCESS_TOKEN']
        self.access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    def get_conn(self):
        conn = twitter.Api(consumer_key=[self.consumer_key],
                            consumer_secret=[self.consumer_secret],
                            access_token_key=[self.access_token_key],
                            access_token_secret=[self.access_token_secret])

        return conn

    def post_message(handle, message):
        conn = Tweet.get_conn()
        conn.PostUpdate(message)
