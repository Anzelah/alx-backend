#!/usr/bin/env python3
"""Create simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """A helper function that returns starting and ending index"""
    prev_page = page - 1
    start_idx = prev_page * page_size
    end_idx = page_size * page

    return (start_idx, end_idx)
