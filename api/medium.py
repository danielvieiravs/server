import requests
import xmltodict

from xml.parsers.expat import ExpatError


def get_posts(user_id):
    """Function to retrieve posts from a user

    Args:
        user_id (str): Medium User Id

    Returns:
        Fail: None, error
        Success: Posts, None
    """
    response = requests.get(f"https://medium.com/feed/{user_id}")

    try:
        xpars = xmltodict.parse(response.text)

    except ExpatError as error:
        return None, error.args[0]

    else:
        item = xpars["rss"]["channel"]["item"]

        if isinstance(item, list):
            items = item

        else:
            items = [item]

        return items, None
