from datetime import datetime, timedelta
import os
import tweepy

DIARY_DIR = 'dailynote'
DIARY_WEB_URL = 'https://tick-taku.com'

def get_latest_diary_filename(date):
  return f'{date.year}/{date.month}/{date:%Y_%-m_%d}'

def is_diary_update(date):
  latest_diary = get_latest_diary_filename(yesterday)
  return os.path.exists(f'{DIARY_DIR}/{latest_diary}.md')

def post_tweet(date):
  client = tweepy.Client(
    consumer_key = os.environ.get('TWITTER_API_KEY'),
    consumer_secret = os.environ.get('TWITTER_API_SECRET'),
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN'),
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
  )
  latest_diary = get_latest_diary_filename(yesterday)
  message = f'{DIARY_WEB_URL}/{DIARY_DIR.lower()}/{latest_diary}'
  print(client.create_tweet(text = message))

yesterday = datetime.now() - timedelta(1)
if is_diary_update(yesterday):
  print('INFO - Diary update found.')
  post_tweet(yesterday)
