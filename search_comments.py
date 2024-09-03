import praw
import config
from config import username, password, client_id, client_secret
ask_subreddit_name = str(input("Which subreddit you want to search (no all)?: "))
key_word_to_search = str(input("What is the keyword you want to search?: "))

def reddit_login():
    try:
        r = praw.Reddit(
            username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent="Comment hunter v0.1"
        )
        # Test the authentication by getting the user's identity
        r.user.me()
        print("Authentication successful!")
        return r
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None  # Return None if authentication fails


def run_bot(r):
    if r is None:
        print("Bot did not authenticate. Exiting...")
        return

    subreddit_name = ask_subreddit_name  # Replace with your desired subreddit
    subreddit = r.subreddit(subreddit_name)

    try:
        for comment in subreddit.comments(limit=25):
            if key_word_to_search in comment.body.lower():
                post = comment.submission
                print(f"Title of the comment ({post.title})")
                print(f"Post URL is {post.url}")
    except Exception as e:
        print(f"Error accessing subreddit '{subreddit_name}': {e}")


# Login to Reddit and run the bot
r = reddit_login()
run_bot(r)
