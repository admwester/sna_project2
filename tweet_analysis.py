""" Tools for analyzing Tweets in the FakeNewsNet dataset:  https://github.com/KaiDMML/FakeNewsNet

Only the tweet datapoints are processed in this module, thus they contain comprehensive information also about the users.
"""

import os
import json
import pandas as pd



class TweetData:
    """ Class for retrieving and analyzing FakeNewsNet Twitter data from a specified dataset folder
    using pandas.DataFrames
    """
    index=["gossipcop/real", "gossipcop/fake", "politifact/real", "politifact/fake"]

    def __init__(self, dir):
        self.load_data(dir)
        self.analyze_key_data()
        self.analyze_retweet_data()
        self.analyze_follower_data()
        self.analyze_following_data()
    
    def load_data(self, dir):
        if not os.path.isdir("csv/"):
            os.mkdir("csv")
        if os.path.exists("csv/gossipcop_real_tweets.csv"):         # Gossipcop real
            self.gc_real_tweets = pd.read_csv("csv/gossipcop_real_tweets.csv", index_col=0)
            self.gc_real_users = pd.read_csv("csv/gossipcop_real_users.csv", index_col=0)
        else:
            self.gc_real_tweets, self.gc_real_users = create_dataframes(os.path.join(dir, "gossipcop/real"))
            self.gc_real_tweets.to_csv("csv/gossipcop_real_tweets.csv")
            self.gc_real_users.to_csv("csv/gossipcop_real_users.csv")

        if os.path.exists("csv/gossipcop_fake_tweets.csv"):         # Gossipcop fake
            self.gc_fake_tweets = pd.read_csv("csv/gossipcop_fake_tweets.csv", index_col=0)
            self.gc_fake_users = pd.read_csv("csv/gossipcop_fake_users.csv", index_col=0)
        else:
            self.gc_fake_tweets, self.gc_fake_users = create_dataframes(os.path.join(dir, "gossipcop/fake"))
            self.gc_fake_tweets.to_csv("csv/gossipcop_fake_tweets.csv")
            self.gc_fake_users.to_csv("csv/gossipcop_fake_users.csv")

        if os.path.exists("csv/politifact_real_tweets.csv"):        # Politifact real
            self.pf_real_tweets = pd.read_csv("csv/politifact_real_tweets.csv", index_col=0)
            self.pf_real_users = pd.read_csv("csv/politifact_real_users.csv", index_col=0)
        else:
            self.pf_real_tweets, self.pf_real_users = create_dataframes(os.path.join(dir, "politifact/real"))
            self.pf_real_tweets.to_csv("csv/politifact_real_tweets.csv")
            self.pf_real_users.to_csv("csv/politifact_real_users.csv")

        if os.path.exists("csv/politifact_fake_tweets.csv"):        # Politifact fake
            self.pf_fake_tweets = pd.read_csv("csv/politifact_fake_tweets.csv", index_col=0)
            self.pf_fake_users = pd.read_csv("csv/politifact_fake_users.csv", index_col=0)
        else:
            self.pf_fake_tweets, self.pf_fake_users= create_dataframes(os.path.join(dir, "politifact/fake"))
            self.pf_fake_tweets.to_csv("csv/politifact_fake_tweets.csv")
            self.pf_fake_users.to_csv("csv/politifact_fake_users.csv")


    def analyze_key_data(self): 
        data = {}
        data["number of tweets"] = [
            self.gc_real_tweets.shape[0], 
            self.gc_fake_tweets.shape[0], 
            self.pf_real_tweets.shape[0], 
            self.pf_fake_tweets.shape[0]
            ]

        data["number of retweets"] = [
            self.gc_real_tweets["retweets"].sum(), 
            self.gc_fake_tweets["retweets"].sum(), 
            self.pf_real_tweets["retweets"].sum(), 
            self.pf_fake_tweets["retweets"].sum()
            ]
        
        data["number of distinct users"] = [
            self.gc_real_users.shape[0],
            self.gc_fake_users.shape[0], 
            self.pf_real_users.shape[0], 
            self.pf_fake_users.shape[0]
            ]

        self.key_data = pd.DataFrame(data=data,index=self.index)
    

    def analyze_retweet_data(self):
            data = {}
            data["mean of retweets/user"] = [
                self.gc_real_users["retweets"].mean(),
                self.gc_fake_users["retweets"].mean(),
                self.pf_real_users["retweets"].mean(),
                self.pf_fake_users["retweets"].mean()
            ]
            data["std of retweets/user"] = [
                self.gc_real_users["retweets"].std(),
                self.gc_fake_users["retweets"].std(),
                self.pf_real_users["retweets"].std(),
                self.pf_fake_users["retweets"].std()
            ]
            data["kurtosis of retweets/user"] = [
                self.gc_real_users["retweets"].kurtosis(),
                self.gc_fake_users["retweets"].kurtosis(),
                self.pf_real_users["retweets"].kurtosis(),
                self.pf_fake_users["retweets"].kurtosis()
            ]

            data["skewness of r/u"] = [
                self.gc_real_users["retweets"].skew(),
                self.gc_fake_users["retweets"].skew(),
                self.pf_real_users["retweets"].skew(),
                self.pf_fake_users["retweets"].skew()
            ]
            self.retweet_data = pd.DataFrame(data=data,index=self.index)
        

    def analyze_follower_data(self):
            data = {}
            data["mean of followers/user"] = [
                self.gc_real_users["followers"].mean(),
                self.gc_fake_users["followers"].mean(),
                self.pf_real_users["followers"].mean(),
                self.pf_fake_users["followers"].mean()
            ]
            data["std of followers/user"] = [
                self.gc_real_users["followers"].std(),
                self.gc_fake_users["followers"].std(),
                self.pf_real_users["followers"].std(),
                self.pf_fake_users["followers"].std()
            ]
            data["kurtosis of followers/user"] = [
                self.gc_real_users["followers"].kurtosis(),
                self.gc_fake_users["followers"].kurtosis(),
                self.pf_real_users["followers"].kurtosis(),
                self.pf_fake_users["followers"].kurtosis()
            ]

            data["skewness of followers/user"] = [
                self.gc_real_users["followers"].skew(),
                self.gc_fake_users["followers"].skew(),
                self.pf_real_users["followers"].skew(),
                self.pf_fake_users["followers"].skew()
            ]
            self.follower_data = pd.DataFrame(data=data,index=self.index)


    def analyze_following_data(self):
            data = {}
            data["mean of following/user"] = [
                self.gc_real_users["following"].mean(),
                self.gc_fake_users["following"].mean(),
                self.pf_real_users["following"].mean(),
                self.pf_fake_users["following"].mean()
            ]
            data["std of following/user"] = [
                self.gc_real_users["following"].std(),
                self.gc_fake_users["following"].std(),
                self.pf_real_users["following"].std(),
                self.pf_fake_users["following"].std()
            ]
            data["kurtosis of followers/user"] = [
                self.gc_real_users["following"].kurtosis(),
                self.gc_fake_users["following"].kurtosis(),
                self.pf_real_users["following"].kurtosis(),
                self.pf_fake_users["following"].kurtosis()
            ]

            data["skewness of following/user"] = [
                self.gc_real_users["following"].skew(),
                self.gc_fake_users["following"].skew(),
                self.pf_real_users["following"].skew(),
                self.pf_fake_users["following"].skew()
            ]
            self.following_data = pd.DataFrame(data=data,index=self.index)

    def get_key_data(self):
        return self.key_data

    def get_retweet_data(self):
            return self.retweet_data

    def get_follower_data(self):
            return self.follower_data

    def get_following_data(self):
            return self.following_data
    
    def get_following_distribution(self):
        # TODO
        pass
    
    def get_follower_distribution(self):
        # TODO
        pass


def create_dataframes(path):
    """Returns two dataframes first containing tweets and the second user attributes
    of the given FakeNewsNet dataset folder ([gossipcop, politifact]/[real,fake]).
    """
    tweet_ids =[]
    likes = []
    retweets = []
    users = []
    followers = []
    following = []
    for dir in os.listdir(path):
        tweet_path = os.path.join(path, dir, "tweets")
        for file in os.listdir(tweet_path):
            file_path = os.path.join(tweet_path, file)
            data = json.load(open(file_path))
            tweet_ids.append(data["id"])
            retweets.append(data["retweet_count"])
            likes.append(data["favorite_count"])
            users.append(data["user"]["id"])
            followers.append(data["user"]["followers_count"])
            following.append(data["user"]["friends_count"])
    tweet_df = pd.DataFrame({
        "id" : tweet_ids, 
        "retweets" : retweets, 
        "likes" : likes, 
        "user" : users, 
        "user followers" : followers, 
        "user following": following
        })
    
    # User dataframe
    user_tweet_count = []
    user_retweet_count = []
    user_likes_count = []
    user_followers_count = []
    user_following_count = []
    tweets_grouped = tweet_df.drop("id", axis=1).groupby("user").sum()
    for id in tweets_grouped.index:
        user_tweet_count.append(tweet_df["user"].value_counts()[id])
        user_retweet_count.append(tweets_grouped["retweets"].loc[id])
        user_likes_count.append(tweets_grouped["likes"].loc[id])

        d = tweet_df[tweet_df["user"] == id].iloc[0]
        user_followers_count.append(d["user followers"] )
        user_following_count.append(d["user following"])

    user_df = pd.DataFrame({"id": tweets_grouped.index, 
        "tweets":user_tweet_count,
        "retweets":user_retweet_count,
        "likes":user_likes_count,
        "followers": user_followers_count,
        "following": user_following_count
        })

    return tweet_df, user_df



if __name__ == "__main__":
    pass