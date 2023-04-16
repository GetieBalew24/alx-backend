#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """deletion hypermedia pagination """
        data_set = self.indexed_dataset()
        assert type(index) is int and index in range(len(data_set))
        datas = []
        first, last = index, index + page_size

        while first < last:
            if first in data_set.keys():
                datas.append(data_set[first])
            else:
                last += 1
            first += 1

        return {
                "index": index,
                "data": datas,
                "page_size": len(datas),
                "next_index": last
                }