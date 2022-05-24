import matplotlib.pyplot as plt
import numpy as np
from tweet_analysis import TweetData

def visualize_key_attributes(tweet_data):
    key_data = tweet_data.get_key_data()
    retweet_data = tweet_data.get_retweet_data()
    follower_data = tweet_data.get_follower_data()
    following_data = tweet_data.get_following_data()

    fig, ax = plt.subplots(4, 1, figsize = (10, 8))
    fig.patch.set_visible(False)
    font_size = 7


    ax[0].axis('off')
    ax[0].axis('tight')
    ax[0].set_title("Overview of the dataset")
    table1 = ax[0].table(cellText=key_data.values, rowLabels=key_data.index, colLabels=key_data.columns, loc="center")
    table1.auto_set_font_size(False)
    table1.set_fontsize(font_size)

    ax[1].axis('off')
    ax[1].axis('tight')
    ax[1].set_title("Retweet metrics")
    table2 = ax[1].table(cellText=retweet_data.values, rowLabels=retweet_data.index, colLabels=retweet_data.columns, loc = "center")
    table2.auto_set_font_size(False)
    table2.set_fontsize(font_size)

    ax[2].axis('off')
    ax[2].axis('tight')
    ax[2].set_title("Follower metrics")
    table3 = ax[2].table(cellText=follower_data.values, rowLabels=follower_data.index, colLabels=follower_data.columns, loc = "center")
    table3.auto_set_font_size(False)
    table3.set_fontsize(font_size)

    ax[3].axis('off')
    ax[3].axis('tight')
    ax[3].set_title("Following metrics")
    table4 = ax[3].table(cellText=following_data.values, rowLabels=following_data.index, colLabels=following_data.columns, loc = "center")
    table4.auto_set_font_size(False)
    table4.set_fontsize(font_size)
    fig.tight_layout()
    plt.show()

def visualize_user_engagement(data, title):
    yAxis = [data["gc_real"], data["gc_fake"], data["pf_real"], data["pf_fake"]]
    xAxis = ["gc_real", "gc_fake", "pf_real", "pf_fake"]
    plt.title(title)
    plt.xlabel('User group')
    plt.ylabel('Mean engagement')
    plt.bar(xAxis, yAxis, color = ["b", "r", "b", "r"])
    plt.show()

def visualize_follow_distributions(tweet_data):
    follow_distributions = tweet_data.get_follow_distributions()

    follow_distributions = tweet_data.get_follow_distributions()

    follower_data = tweet_data.get_follower_data()
    following_data = tweet_data.get_following_data()

    fig, ax = plt.subplots(2,2)
    ax[0,0].bar(follow_distributions.index[0], follow_distributions["followers"][0], color = 'b')
    ax[0,0].bar(follow_distributions.index[1], follow_distributions["followers"][1], color = 'r')
    ax[0,0].bar(follow_distributions.index[2], follow_distributions["followers"][2], color = 'b')
    ax[0,0].bar(follow_distributions.index[3], follow_distributions["followers"][3], color = 'r')
    ax[0,0].set_title("Sum of followers")

    ax[0,1].bar(follow_distributions.index[0], follower_data["mean of followers/user"][0], color = 'b')
    ax[0,1].bar(follow_distributions.index[1], follower_data["mean of followers/user"][1], color = 'r')
    ax[0,1].bar(follow_distributions.index[2], follower_data["mean of followers/user"][2], color = 'b')
    ax[0,1].bar(follow_distributions.index[3], follower_data["mean of followers/user"][3], color = 'r')
    ax[0,1].set_title("Followers per user")

    ax[1,0].bar(follow_distributions.index[0], follow_distributions["following"][0], color = 'b')
    ax[1,0].bar(follow_distributions.index[1], follow_distributions["following"][1], color = 'r')
    ax[1,0].bar(follow_distributions.index[2], follow_distributions["following"][2], color = 'b')
    ax[1,0].bar(follow_distributions.index[3], follow_distributions["following"][3], color = 'r')
    ax[1,0].set_title("Sum of others followed by users")

    follower_data = tweet_data.get_follower_data()
    ax[1,1].bar(follow_distributions.index[0], following_data["mean of following/user"][0], color = 'b')
    ax[1,1].bar(follow_distributions.index[1], following_data["mean of following/user"][1], color = 'r')
    ax[1,1].bar(follow_distributions.index[2], following_data["mean of following/user"][2], color = 'b')
    ax[1,1].bar(follow_distributions.index[3], following_data["mean of following/user"][3], color = 'r')
    ax[1,1].set_title("Others followed per user")
    plt.show()

def main(dir):
    tweet_data = TweetData(dir)
    visualize_key_attributes(tweet_data)
    visualize_follow_distributions(tweet_data)
    visualize_user_engagement(tweet_data.user_engagements_P1, "Mean user engagement 2022/01 - 2022/04")
    visualize_user_engagement(tweet_data.user_engagements_P2, "Mean user engagement 2021/05 - 2022/05")
    visualize_user_engagement(tweet_data.user_engagements_P3, "Mean user engagement 2019/05 - 2022/05")    

if __name__ == "__main__":

    main("fakenewsnet_dataset_sample")