import pytest
import main
import praw
import os
from dotenv import load_dotenv
import shutil
load_dotenv()


# TODO just run the Reddit app once and do all the checkings, needs research on the pytest settings
def test_type_function():
    try:
        shutil.rmtree('output')
    except:
        pass
    reddit = praw.Reddit(client_id=os.getenv('API_ID'),
        client_secret=os.getenv('API_SECRET'),
        user_agent=os.getenv('USER_AGENT'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PSSWD'))
    subreddit = 'tattoo'
    assert type(main.getting_tattoo_pictures(reddit, subreddit)) == int


def test_exists_image_files():
    try:
        shutil.rmtree('output')
    except:
        pass
    reddit = praw.Reddit(client_id=os.getenv('API_ID'),
        client_secret=os.getenv('API_SECRET'),
        user_agent=os.getenv('USER_AGENT'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PSSWD'))
    subreddit = 'tattoo'
    main.getting_tattoo_pictures(reddit, subreddit)
    assert os.path.isfile('output/tattoo_1.jpg') == True 