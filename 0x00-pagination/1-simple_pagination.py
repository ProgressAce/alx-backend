#!/usr/bin/env python3
"""Contains a class that paginates data from a dataset."""

import csv
import math
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of all the items for a particular page of the dataset

        Verifies that both arguments are integers greater than 0.

        Dependencies:
            index_range: provides the needed start and end indexes of
            the dataset to retrieve the right items.
        """

        assert type(page) == int and type(page_size) == int 
        assert page > 0 and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        self.dataset()  # ensure dataset is cached

        try:  # for python versions where indicing outer range raises error
            return self.__dataset[start_idx: end_idx]
        except IndexError as e:
            return []


def index_range(page: int, page_size: int) -> Tuple:
    """
    Gives the start and end indexes of a page according to page number
    and size.

    Example:
    user@desktop:~$ cat 0-main.py
        #!/usr/bin/env python3

        index_range = __import__('0-simple_helper_function').index_range
        
        res = index_range(1, 7)
        print(type(res))
        print(res)

        res = index_range(page=3, page_size=15)
        print(type(res))
        print(res)

    user@desktop:~$ ./0-main.py
        <class 'tuple'>
        (0, 7)
        <class 'tuple'>
        (30, 45)
    """

    if page < 1:
        return (-1, -1)
    
    start_idx = page * page_size - page_size
    end_idx = page * page_size

    return (start_idx, end_idx)
