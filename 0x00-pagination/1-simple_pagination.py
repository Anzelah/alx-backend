#!/usr/bin/env python3
"""Implement pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """A helper function that returns starting and ending index"""
    prev_page = page - 1
    start_idx = prev_page * page_size
    end_idx = page_size * page

    return (start_idx, end_idx)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            assert type(page) == int and type(page_size) == int
            assert page > 0 and page_size > 0
            
            indexes = index_range(page, page_size)
            data = self.dataset()
            if page < 0 and page >= len(data) or page_size < 0 and page_size >= len(data):
                return []
            return data[indexes[0]:indexes[1]]
