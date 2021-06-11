"""Helper methods."""
# third-party imports
import requests
import logging

logger = logging.getLogger(__name__)


def make_request(url, params=None):
    """
    Helper method that uses Python Requests library to make calls to
    external APIs
    :param url: url on which request can make
    :return: data returned by requests library in the json format
    """
    results = []
    try:
        res = requests.get(url, params)
    except Exception:
        logger.exception(f"Exception occurred for url {url} with {params}.")
    else:
        if res.status_code == 200 and res.text:
            results = res.json()
            logger.info(f"Fetched {len(results)} records from the url {url} with {params}.")
        elif res.status_code == 404:
            logger.info(f"No record found against url {url} with {params}.")
        elif res.status_code == 400:
            logger.info(f"Invalid request made against url {url} with {params}")
        elif res.status_code == 500:
            logger.error(f"Unable to get response from url {url} with {params}.")

    return results
