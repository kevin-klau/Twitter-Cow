iimport os
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


tweets_list1 = set()

# Using TwitterSearchScraper to scrape data and append tweets to list
hashtag : str

with open('ScrapedInfo.txt', 'w', encoding='utf-8') as f:

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('hashtag').get_items()):
        if i>500:
            break
        info = tweet.content + 'とチ.く$' + str(tweet.replyCount) + 'とチ.く$' + str(tweet.likeCount) + 'とチ.く$' + str(tweet.retweetCount) + 'とチ.く$' + str(tweet.quoteCount) + 'とチ.く$' + str(tweet.viewCount) + 'ン'
        for i in info : 
            if ord(i) == 32 or ord(i) == 35:
                continue
            elif ord(i) == 12531:
                break
            else:
                f.write(i)




                