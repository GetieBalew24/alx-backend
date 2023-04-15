#!/usr/bin/env python3
""" Task 0, a function named index_range that takes two integer arguments page and page_size
a function return a tuple of size two containing a start index and an end index
to the range of indexes to return in a list for those particular pagination parameters.
"""
def index_range(page: int, page_size: int) -> tuple:
    """
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    indexOfrange = first_index, last_index
    return indexOfrange