import datetime
from utility import read_settings, get_keywords, daterange
from web_scraper import get_comments
import pandas as pd
from dictionary_sentiment_analysis import dictionary_sentiment_check
import numpy


settings = read_settings('settings.txt')
keywords = get_keywords(settings[0])
print(keywords)

df = pd.DataFrame()

for start_date in daterange(settings[1], settings[2]):
    end_date = start_date + datetime.timedelta(days=1)
    for subreddit in settings[-1]:
        print("Checking " + subreddit)
        df = df.append(get_comments(subreddit, start_date, end_date, keywords))

vectorized_sentiment_check = numpy.vectorize(dictionary_sentiment_check)
df['Dictionary_bullishness'] = vectorized_sentiment_check(df['Body'])

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print(df)

dictionary_metric = df.drop(columns=['ID', 'Author', 'Body'])

print(dictionary_metric)

insights = []

for subreddit in dictionary_metric['Subreddit'].tolist():
    insights.append(dictionary_metric[dictionary_metric['Subreddit'] == subreddit])

