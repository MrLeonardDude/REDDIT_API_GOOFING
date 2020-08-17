"""Python API Wrapper Learning Session
"""
from dotenv import load_dotenv
import os
import praw
import click


@click.command()
@click.option('--subreddits', default="tattoo", help="List of Subreddits you are interested in searching!")
def main(subreddits):
    """script main function
    """
    print(f"Your choices were {subreddits}")
    reddit = praw.Reddit(client_id=os.getenv('API_ID'),
                     client_secret=os.getenv('API_SECRET'),
                     user_agent=os.getenv('USER_AGENT'),
                     username=os.getenv('REDDIT_USERNAME'),
                     password=os.getenv('REDDIT_PSSWD'))
    sub = reddit.subreddit(subreddits)
    for i, submission in enumerate(sub.hot(limit=10)):
        author = submission.author
        print(f"#{i} - {submission.title}")
        print(f"Author {author.name}")
        print(f"Text {submission.selftext}")
        print("-----------")
    


if __name__ == "__main__":    
    load_dotenv()
    main()
