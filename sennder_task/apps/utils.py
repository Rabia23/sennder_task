"""Helper methods"""

# third-party imports
import requests


def make_request(url, params=None):
    """
    Helper method that uses Python Requests library to make calls to
    external APIs
    :param url: url on which request can make
    :return: data returned by requests library in the json format
    """

    # handle exceptions later
    resp = requests.get(url, params)
    results = []
    # manual retries to 1
    if resp.status_code == 200:
        # if youtube_response.status_code == 200 and youtube_response.text:
        # if we have 200 response and list is empty
        results = resp.json()
        print(len(results))
        print(results[0])
    return results
