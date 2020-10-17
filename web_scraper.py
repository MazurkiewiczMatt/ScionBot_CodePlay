import datetime
import pandas as pd
import praw
import json
import requests
from passcodes import passcodes

r = praw.Reddit(client_id=passcodes["client_id"],
                client_secret=passcodes["client_secret"],
                password=passcodes["password"],
                user_agent=passcodes["user_agent"],
                username=passcodes["username"])


def getPushshiftData(after, before, sub):
    # gets dictionary of all submissions and their ids
    url = 'https://api.pushshift.io/reddit/search/submission/?after=' + str(after) + '&before=' + str(
        before) + '&subreddit=' + str(sub)
    req = requests.get(url)
    data = json.loads(req.text)
    return data['data']


def comment_to_df(comment):
    new_row = pd.Series(
        [datetime.date.fromtimestamp(comment.created_utc), comment.id, comment.author, comment.subreddit, comment.body])
    # what elements of the comment to add to dataframe
    return pd.DataFrame([new_row])


def get_comments(subreddit, start_date, end_date, keywords=[]):
    df = pd.DataFrame()

    submissions = getPushshiftData(start_date, end_date, subreddit)
    print("pushift data got!")

    for submission in submissions:
        print("checking submission!")
        post = r.submission(id=submission["id"])
        post.comments.replace_more(limit=0)
        comment_queue = post.comments[:]
        if keywords == []:
            while comment_queue:
                comment = comment_queue.pop(0)
                df = pd.concat([comment_to_df(comment), df], ignore_index=True)
                comment_queue.extend(comment.replies)
        else:
            while comment_queue:
                comment = comment_queue.pop(0)
                if any(keyword in comment.body.lower() for keyword in keywords):
                    df = pd.concat([comment_to_df(comment), df], ignore_index=True)
                comment_queue.extend(comment.replies)

    df = df.rename(columns={0: "Date", 1: "ID", 2: "Author", 3: "Subreddit", 4: "Body"})
    print("done!")
    return df
