import praw
import config
from config import username, password, client_id, client_secret
ask_subreddit_name = str(input("Which subreddit you want to search?: "))
key_word_to_search = str(input("What is the keyword you want to search?: "))

def reddit_login():
    try:
        r = praw.Reddit(
            username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent="Post hunter v0.1"
        )
        r.user.me()  # Test authentication
        print("Authentication successful!")
        return r
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None


def find_latest_posts(r):
    if r is None:
        print("Bot did not authenticate. Exiting...")
        return

    subreddit_name = ask_subreddit_name
    subreddit = r.subreddit(subreddit_name)

    try:
        # Search for the latest posts containing e.g "Python"
        for submission in subreddit.search(key_word_to_search, sort="new", limit=25):
            print(f"Found a post in (r/{submission.subreddit.display_name}): {submission.title}")
            print(f"URL: {submission.url}\n")
    except Exception as e:
        print(f"Error accessing subreddit '{subreddit}': {e}")


# Login to Reddit and find the latest posts with e.g "Python" in the title
r = reddit_login()
find_latest_posts(r)
