import datetime
import os
import tweepy

DIARY_DIR = 'DailyNotes'
DIARY_WEB_URL = 'https://tick-taku.com'

def get_todays_diary_path():
  now = datetime.datetime.now()
  return f'{now.year}/{now.month}/{now:%Y_%-m_%d}'

def is_diary_updated(path):
  return os.path.exists(f'{DIARY_DIR}/{path}.md')

def post_tweet(path):
  client = tweepy.Client(
    consumer_key = os.environ.get('TWITTER_API_KEY'),
    consumer_secret = os.environ.get('TWITTER_API_SECRET'),
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN'),
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
  )
  message = f'{os.path.basename(path)}\n{DIARY_WEB_URL}/{DIARY_DIR.lower()}/{path}'
  print(client.create_tweet(text = message))

todays_path = get_todays_diary_path()
if is_diary_updated(todays_path):
  print('INFO - Diary update found.')
  post_tweet(todays_path)
