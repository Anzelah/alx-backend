#!/usr/bin/env python3
"""Implement pagination"""

import csv
import math
from typing import List, Dict


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
        """Initialize instances
        """
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
        """Paginate your dataset which is a list containing popular names
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        index = index_range(page, page_size)
        data = self.dataset()
        if not 0 <= page < len(data) or not 0 <= page_size < len(data):
            return []
        return data[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Return a hateoas dict
        """
        index = index_range(page, page_size)
        all_data = self.dataset()
        returned_data = all_data[index[0]:index[1]]
        total = len(all_data)

        prev = page - 1
        nxt = page + 1
        total_pages = (total + page_size - 1) // page_size

        return {
                'page_size': len(returned_data),
                'page': page,
                'data': returned_data,
                'next_page': None if page >= total_pages else nxt,
                'prev_page': None if prev is 0 else prev,
                'total_pages': total_pages
                }
