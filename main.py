"""Python API Wrapper Learning Session
"""
from dotenv import load_dotenv
import os
import praw
import shutil
import click
import requests


def download_file(url: str, ext: str, iter: int):
    r = requests.get(url, stream=True)
    with open(f'output/tattoo_{iter}.{ext}', 'wb+') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)


def getting_tattoo_pictures(reddit: praw.Reddit, subreddits: str):
    """Given the Tattoo Subreddit, we will download all the tattoo pictures

    Args:
        reddit (praw.Reddit): API Reddit Class
        subreddits (str): Name of the subreddit

    Returns:
        int: Number of images that have been downloaded
    """
    sub = reddit.subreddit(subreddits)
    os.mkdir('output')
    count_images = 0
    for i, submission in enumerate(sub.hot(limit=30)):
        ext = submission.url.split('.')[-1]
        # TODO add different extensions
        if 'jpg' in ext:
            count_images += 1
            download_file(submission.url, ext, count_images)
    return count_images
        


@click.command()
@click.option('--subreddits', default="tattoo", help="List of Subreddits you are interested in searching!")
def main(subreddits: str):
    """script main function
    """
    try:
        shutil.rmtree('output')
    except:
        pass
    print(f"Your choices were {subreddits}")
    reddit = praw.Reddit(client_id=os.getenv('API_ID'),
                     client_secret=os.getenv('API_SECRET'),
                     user_agent=os.getenv('USER_AGENT'),
                     username=os.getenv('REDDIT_USERNAME'),
                     password=os.getenv('REDDIT_PSSWD'))
    if 'tattoo' in subreddits:
        images_downloaded = getting_tattoo_pictures(reddit, subreddits)
        print(f"We have downloaded {images_downloaded} images")



if __name__ == "__main__":
    load_dotenv()
    main()
