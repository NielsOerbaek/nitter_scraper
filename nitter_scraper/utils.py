"""Module for scraping tweets"""
from datetime import datetime
import re
from typing import Dict, Optional

from requests_html import HTMLSession

from nitter_scraper.schema import Tweet  # noqa: I100, I202

def user_exists(
    username: str,
    address="https://nitter.net",
) -> bool:
    """ Checks if a user exists on nitter """
    
    url = f"{address}/{username}"
    session = HTMLSession()

    response = session.get(url)
    title = response.html.find("title", first=True).text
    return not title == "Error | nitter"
    
def username_from_url(url: str) -> str:
    """ Extracts a username from a url """
    if "/" not in url:
        # If the url contains no slashes, it is probably a username
        return url
    username = re.search(r"(?:https?:\/\/)?(?:www\.)?(?:mobile\.)?twitter\.com\/([a-zA-Z0-9_]+)", url)
    if username:
        return username.group(1)
    else:
        return None