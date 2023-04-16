#!/usr/bin/env python3
"""index_range from the previous task to `Server` class """
import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names. """
    Data = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.Data) as f:
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
        return items for the given page number range
        Args:
            page (int): the current page number
            page_size (int): number of rows per page
        Returns:
            (List[List]): a list of row if page and page size > 0
            ([]) : an empty list if page and page_size < 0
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        FirstIndex, LastIndex = self.index_range(page, page_size)
        return self.dataset()[FirstIndex:LastIndex]
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """hypermedia pagination"""
        data_set = self.get_page(page, page_size)
        prev_pages = page - 1 if page > 1 else None
        next_pages = page + 1 if page < total_page else None
        total_page = math.ceil(len(self.dataset()) / page_size)
        return {
                "page_size": len(data_set),
                "page": page,
                "data": data_set,
                "next_page": next_pages,
                "prev_page": prev_pages,
                "total_pages": total_page
                }
