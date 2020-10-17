from datetime import date
from utility import read_settings, get_keywords
from web_scraper import get_comments
import pandas

settings = read_settings('settings.txt')
keywords = get_keywords(settings[0])

dataframes = []

for subreddit in settings[-1]:
    dataframes.append(get_comments(subreddit, settings[1], settings[2], keywords))

df = dataframes[0]
for dfs in range(len(dataframes) - 1):
    df.append(dataframes[dfs+1])

print(df)
