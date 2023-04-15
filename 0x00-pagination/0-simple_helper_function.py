#!/usr/bin/env python3
"""
Module 0-simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page
    """
    index_tuple = page_size * (page - 1), page * page_size
    return index_tuple