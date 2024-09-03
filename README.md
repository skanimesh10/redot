# Reddit Search Bot

This project contains Python scripts for searching Reddit posts and comments using the PRAW (Python Reddit API Wrapper) library.

## Features

- Authenticate with Reddit API
- Search for posts in a specific subreddit by keyword
- Search for comments in a specific subreddit by keyword

## Files

- `config.py`: Contains configuration settings and credentials
- `search_posts.py`: Script to search for posts in a subreddit
- `search_comments.py`: Script to search for comments in a subreddit

## Setup

1. Install the required library:

2. Update the `config.py` file with your Reddit API credentials:
- username
- password
- client_id
- client_secret

## Usage

### Searching Posts

Run the `search_posts.py` script:

You will be prompted to enter:
- The subreddit name you want to search
- The keyword you want to search for

The script will then display the latest 25 posts containing the keyword.

### Searching Comments

Run the `search_comments.py` script:

You will be prompted to enter:
- The subreddit name you want to search (excluding "all")
- The keyword you want to search for

The script will then display the latest 25 comments containing the keyword.

## Note

Make sure to comply with Reddit's API terms of service and usage guidelines when using this bot.
