#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__("0-simple_helper_function").index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res[0]))
print(res)

# extra cases
# invalid page number (page nums start at 1) (does not factor max page number)
print(index_range(0, 4))

# invalid page_size
print(index_range(0, 0))
