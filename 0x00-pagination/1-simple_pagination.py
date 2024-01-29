#!/usr/bin/env python3
"""Defines a class that paginates its data."""

import csv
import math
from typing import List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Obtains the correct data from the paginated data for the given page.

        Args:
            page: the current to get the data from.
            page_size: the number of items in each page.

        Returns:
            the appropriate page of the dataset."""

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        idx_range: int = index_range(page, page_size)
        start: int = idx_range[0]
        end: int = idx_range[1]

        self.dataset()
        page_data: List[List[str]] = self.__dataset[start:end]

        return page_data
