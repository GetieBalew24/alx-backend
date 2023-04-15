#!/usr/bin/env python3
"""
Adds `get_page` method to `Server` class
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number
        Args:
            page (int): page number
            page_size (int): number of items per page
        Returns:
            (List[List]): a list of list(row) if inputs are within range
            ([]) : an empty list if page and page_size are out of range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]

