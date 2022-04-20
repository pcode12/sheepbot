import praw
from praw.models import MoreComments
import pandas as pd

reddit = praw.Reddit(
    client_id = "8GG53Au_174E9wNThz_QxA", 
    client_secret = "p9_s3UCSeqyRYImHsOb6C9irLmDLDg", 
    user_agent = "CraftScraper"
)

def craftSearch(craft):
    post_df = pd.DataFrame()
    top_10_titles = []
    top_10_links = []
    craft = craft.lower()
    sub = reddit.subreddit(craft)

    if craft == "cross stitch":
        craft = "CrossStitch"


    if craft == "crochet" or craft == "knitting":
        for post in sub.search('flair:"Finished Object"', sort="hot", time_filter="week", limit=11):
            top_10_titles.append(post.title)
            top_10_links.append(post.permalink)
    elif craft == "embroidery":
        for post in sub.search('flair:"Hand"', sort="hot", time_filter="week", limit=11):
            top_10_titles.append(post.title)
            top_10_links.append(post.permalink)
    elif craft == "CrossStitch":
        for post in sub.search('flair:"FO"', syntax="lucene", sort="hot", time_filter="week", limit=11):
            top_10_titles.append(post.title)
            top_10_links.append(post.permalink)

    post_df["Titles"] = top_10_titles
    post_df["Links"] = top_10_links

    return post_df

if __name__ == "__main__":
    userIn = input("What craft would you like to search for? ")
    craft_df = craftSearch(userIn)
    print(craft_df)





 