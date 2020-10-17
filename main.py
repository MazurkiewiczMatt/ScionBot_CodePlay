from datetime import date
from utility import read_settings, get_keywords
from web_scraper import get_comments
import pandas as pd
from dictionary_sentiment_analysis import dictionary_sentiment_check
import numpy


settings = read_settings('settings.txt')
keywords = get_keywords(settings[0])
print(keywords)

df = pd.DataFrame()

for subreddit in settings[-1]:
    print("Checking " + subreddit)
    df = df.append(get_comments(subreddit, settings[1], settings[2], keywords))

vectorized_sentiment_check = numpy.vectorize(dictionary_sentiment_check)
df['Dictionary_bullishness'] = vectorized_sentiment_check(df['Body'])

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print(df)

dictionary_metric = df.drop(columns=['ID', 'Author', 'Body'])

print(dictionary_metric)

