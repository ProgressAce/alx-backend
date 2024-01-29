#!/usr/bin/env python3
"""Defines a class that paginates its data."""

import csv
import math
from typing import List, Optional

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
        page_data = self.__dataset[start:end]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Obtains the correct data from the paginated data for the given page,
        plus additional navigation information.

        Args:
            page: the current to get the data from.
            page_size: the number of items in each page.

        Returns:
            a dictionary containing the information of the page data and
            further page navigation."""

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        idx_range: int = index_range(page, page_size)
        start: int = idx_range[0]
        end: int = idx_range[1]

        self.dataset()
        page_data: List[List[str]] = self.__dataset[start:end]

        total_items = len(self.__dataset)

        # additional hypermedia (further page navigation) info
        total_pages: int = (total_items + page_size - 1) // page_size

        if (page + 1) <= total_pages:
            next_page: Optional[int] = page + 1
        else:
            next_page = None

        if (page - 1) > 0:  # page index starts at 1
            prev_page: Optional[int] = page - 1
        else:
            prev_page = None

        return {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
