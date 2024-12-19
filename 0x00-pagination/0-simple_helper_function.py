#!/usr/bin/env python3
"""Define function that gives the start and end indexes of a page's items"""

from typing import Tuple


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
