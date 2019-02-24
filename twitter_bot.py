import tweepy
import pandas as pd
import numpy as np
import json


def twitter_setup(key_file):
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    with open(key_file) as f:
        data = json.load(f)

    CONSUMER_KEY = data["consumer_API"]["key"]
    CONSUMER_SECRET = data["consumer_API"]["secret"]
    ACCESS_TOKEN = data["access"]["token"]
    ACCESS_SECRET = data["access"]["secret"]

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def select_tweet(df):
    """

    """
    tweet_number = np.random.randint(0, df.shape[0]-1)

    tweet = df.iloc[tweet_number]

    return tweet.values[0], tweet_number


def publish_tweet(tweet, api):

    tweet = add_hashtags(tweet)

    api.update_status(tweet)
    print("publishing tweet {}".format(tweet))


def add_hashtags(tweet):

    for tag in hashtags:
        if len(tweet + " " + tag) < 140:
            tweet = tweet + " " + tag

    return tweet


def update_tweets_file(df, tweet_number):

    df = df.drop(df.index[tweet_number])
    df.to_csv(tweets_file, index=False, encoding="utf-8", header=None)

    return 0


def retweet(df):

    df = df[df["to_tweet"] == 1]

    tweet, tweet_number = select_tweet(df)

    return tweet["quote"]


tweets_file = ".\generated_quotes\quotes_to_tweet.csv"
generated_quotes = ".\generated_quotes\generated_all.csv"

hashtags = ["#DeepLearning", "#AI", "#NLP", "#Inspirational", "#TextGenerator"]

def main():

    api = twitter_setup("twitter_keys.json")
    df = pd.read_csv(tweets_file, header=None)
    if df.shape[0] > 0:
        tweet, tweet_number = select_tweet(df)
        update_tweets_file(df, tweet_number)
        publish_tweet(tweet, api)

    # in case the file is empty just retweet a generated quote
    else:
        print("no more new tweets, re-tweeting")
        df = pd.read_csv(generated_quotes)
        tweet = retweet(df)
        publish_tweet(tweet, api)


if __name__ == "__main__":
    main()