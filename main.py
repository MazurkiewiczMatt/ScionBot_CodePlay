from datetime import date
from utility import read_settings, get_keywords
from web_scraper import get_comments
import pandas

settings = read_settings('settings.txt')
keywords = get_keywords(settings[0])


df = get_comments(settings[-1][0], settings[1], settings[2], keywords)

print(df)
