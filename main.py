"""Python API Wrapper Learning Session
"""
from dotenv import load_dotenv
import os
import praw


def main():
    """script main function
    """
    reddit = praw.Reddit(client_id=os.getenv('API_ID'),
                     client_secret=os.getenv('API_SECRET'),
                     user_agent=os.getenv('USER_AGENT'))
    sub = reddit.subreddit('rust')
    print("------------------------------------------------------------")
    print(sub.title)
    print("------------------------------------------------------------")
    print(sub.description)


if __name__ == "__main__":
    load_dotenv()
    main()
