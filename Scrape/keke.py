import os
import snscrape
import pandas as pd
import snscrape.modules.twitter as sntwitter
import csv

import numpy as np

# Using OS library to call CLI commands in Python
#os.system("snscrape --jsonl --max-results 1000 --since 2021-06-01 twitter-search \"its the elephant until:2021-07-31\" > text-query-tweets.json")

# Reads the json generated from the CLI commands above and creates a pandas dataframe
#tweets_df = pd.read_json('text-query-tweets.json', lines=True)
#tweets_df.to_csv(r'C:\Users\User\Downloads\king.csv', index=False, header=False)


tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('its the elephant since:2020-06-01 until:2020-07-31').get_items()):
    if i>500:
        break
    tweets_list1.append([tweet.content])

print(tweets_list1[0][0])