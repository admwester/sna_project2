import matplotlib.pyplot as plt
from tweet_analysis import TweetData

def visualize(tweet_data):
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


def main(dir):
   
    
    tweet_data = TweetData(dir)
    visualize(tweet_data)
    



    

if __name__ == "__main__":

    main("fakenewsnet_dataset_sample")