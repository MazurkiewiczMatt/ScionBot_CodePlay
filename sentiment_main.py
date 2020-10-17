"""
Created on 17/10/2020

@author: Kamil Iwanowski
"""
import utility
from web_scraper import get_comments
import pandas as pd
import numpy
import datetime
from dictionary_sentiment_analysis import vectorized_sentiment_check
from monkeylearn import MonkeyLearn
ml = MonkeyLearn('f4bbf60d362e38d5897af58b0500519959783001')
model_id = "cl_pi3C7JiL"

keywords = {"msft": ["msft", "microsoft", "gates"], "tsla": ["tsla", "tesla", "musk"],
            "aapl": ["aapl", "apple", "cook"], "fb": ["fb", "facebook", "zuckerberg"],
            "amzn": ["amzn", "amazon", "bezos"], "googl": ["googl", "google", "alphabet", "pichai"]}

settings_file = utility.read_settings("settings.txt")
[company, start_date, end_date, subreddits] = settings_file

# main program, downloads data using reddit API
comments = pd.DataFrame()
for single_date in utility.daterange(start_date, end_date):
    for subreddit in subreddits:
        print("Checking " + str(subreddit) + "on" + str(single_date))
        new_data = get_comments(subreddit, single_date, single_date+datetime.timedelta(days=1), keywords[company])
        comments = comments.append(new_data)

# saves the data if something went wrong, since downloading data is a very long process
comments.to_csv("datasets/"+ str(company) + "_one_week_data.csv")

company_data = comments.reset_index()
company_data = company_data.drop(columns=["index"])
data = company_data["Body"].values.tolist()

# Data analysis using Monkey Learn API
response = ml.classifiers.classify(model_id, data)
company_data["Tag"], company_data["Classifier"] = utility.extract_classification(response.body)
company_data["Dictionary_Tag"] = vectorized_sentiment_check(company_data["Body"])

# Saving the final result
result = company_data.copy()
result = result.drop(columns=["ID", "Author", "Body"])
result.to_csv("results/" + str(company) + "_result_one_week.csv")