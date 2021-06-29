"""Helper methods."""
# third-party imports
import logging

import requests

logger = logging.getLogger(__name__)


def make_request(url, params=None):
    """
    Helper method that uses python requests library to make calls to
    external APIs

    Parameters
    ----------
    url : str
        url on which request can make
    params : dict, optional
        url parameters, by default None

    Returns
    -------
    list
        data returned by requests library in the json format if response code
        is 200, empty list otherwise
    """
    results = []
    try:
        res = requests.get(url, params)
    except Exception:
        logger.exception(f"Exception occurred for url {url} with {params}.")
    else:
        if res.status_code == 200 and res.text:
            results = res.json()
            logger.info(
                f"Fetched {len(results)} records from the url {url} with {params}."  # noqa:501
            )
        elif res.status_code == 404:
            logger.info(f"No record found against url {url} with {params}.")
        elif res.status_code == 400:
            logger.info(
                f"Invalid request made against url {url} with {params}"
            )
        elif res.status_code == 500:
            logger.error(
                f"Unable to get response from url {url} with {params}."
            )

    return results
