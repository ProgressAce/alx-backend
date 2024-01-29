#!/usr/bin/env python3
"""
Main file
"""

import os

Server = __import__("1-simple_pagination").Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, "Bob")
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

cwd = os.getcwd()  # get cwd
files = os.listdir(cwd)  # returns a list of all the files in the given directory
print("----------------------")
print("The files in {}: {}".format(cwd, files))
print("----------------------")

# print(server.dataset())
print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
