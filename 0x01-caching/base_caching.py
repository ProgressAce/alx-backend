#!/usr/bin/python3
"""Base caching module."""

class BaseCaching():
	""" BaseCaching defines:
	  - constants of the cache system
	  - where the data is stored (in a dictionary)"""

	MAX_ITEMS = 4

	def __init__(self):
		""" Initialise the cache object."""
		self.cache_data = {}

	def print_cache(self):
		""" Print the cache."""

		print("Current cache:")
		for key in sorted(self.cache_data.keys()):
			print("{}: {}".format(key, self.cache_data.get(key)))

	def put(self, key, item):
		""" Add an item in the cache."""

		raise NotImplementedError("put must be implemented in your cache class")

	def get(self, key):
		""" Retrieve an item in the cache."""

		raise NotImplementedError("get must be implemented in your cache class")
