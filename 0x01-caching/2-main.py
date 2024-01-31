#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__("2-lifo_cache").LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")  # Key D gets discarded as it is the lastest key
my_cache.print_cache()
my_cache.put("C", "Street")  # Nothing gets discarded as key C is just updated
my_cache.print_cache()
my_cache.put("F", "Mission")  # C gets discarded as it was last updated/inserted
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
