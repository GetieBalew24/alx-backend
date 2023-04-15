#!/usr/bin/env python3
""" Task 0 genrate index range"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Args:
        page (int): the current page
        page_size (int): the size of items in a page
        first_index: calculate the first index
        last_index: calculate the last index 
        indexOfrange: return first index and last index 
    Returns:
        (tuple): a row/tuple of the start and end index of the given page
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    indexOfrange = first_index, last_index
    return indexOfrange
