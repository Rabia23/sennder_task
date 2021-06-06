"""Pagination file."""
from rest_framework.pagination import PageNumberPagination

from sennder_task.settings import PAGE_SIZE


class StandardResultsSetPagination(PageNumberPagination):
    """Standard result set pagination class.

    A simple page number based class that helps you manage the
    paginated data using page numbers in the request query parameters.

    Parameters
    ----------
    PageNumberPagination : rest_framework.pagination
    """

    page_size = PAGE_SIZE
