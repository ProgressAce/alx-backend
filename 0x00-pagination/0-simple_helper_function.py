#!/usr/bin/env python3
"""Defines function that returns the index range of pagination parameters."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the range of the given pagination parameters.

    Args:
        page: the current page.
        page_size: the number of items per page.

    Returns:
        a tuple of 2 integers, representing the start and end indexes (range)
        of the current paginated page."""

    if page < 1 or page_size < 1:
        return (-1, -1)

    start_idx: int = (page - 1) * page_size
    end_idx: int = page * page_size

    return (start_idx, end_idx)
