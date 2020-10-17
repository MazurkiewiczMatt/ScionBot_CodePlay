from datetime import date
from utility import read_settings, get_keywords
from web_scraper import get_comments
import pandas as pd
from dictionary_sentiment_analysis import dictionary_sentiment_check


settings = read_settings('settings.txt')
keywords = get_keywords(settings[0])
print(keywords)

df = pd.DataFrame()

for subreddit in settings[-1]:
    print("Checking " + subreddit)
    df = df.append(get_comments(subreddit, settings[1], settings[2], keywords))

print(df)

df['Dictionary_bullishness'] = df['Body'].apply(dictionary_sentiment_check())
