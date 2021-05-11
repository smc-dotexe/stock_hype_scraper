import praw
import json
import re
import os
from dotenv import load_dotenv

import yfinance as yf
# import yahoo_fin.stock_info as si

load_dotenv(override=True)

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

subred = reddit.subreddit("wallstreetbets") # Enter subreddit here

def ticker_filter(comment):
    pattern = r"[A-Z]{2,4}[\S]"
    comment_ticker_search = re.search(pattern, comment.body)

    if (comment_ticker_search):
        extract_ticker = re.findall(pattern, comment.body)
        for ticker in extract_ticker:
            # ticker_data = si.get_data(ticker)
            try:
                print(ticker)
                print(comment.body)
                ticker_data = yf.Ticker(ticker)
                print(ticker_data.info)
                print("reddit.com"+comment.permalink)
            except:
                pass
            print('==========================')


for comment in subred.stream.comments(skip_existing=True):
    # ticker_filter(comment)
    ticker_filter(comment)
    

