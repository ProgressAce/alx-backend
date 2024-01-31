#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__("1-fifo_cache").FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

print("------------\nAdditional cases:\n------------")
new_cache = FIFOCache()
new_cache.put("Lolipop", "Yogeta")
new_cache.put(None, "Epson")
new_cache.put("Mission", None)
new_cache.put(None, None)
new_cache.print_cache()

# values can be any type
new_cache.put("a", 1)
new_cache.put("b, c", [2, 3])
# dict keys can only be immutable types, but for this cache system printing function
# any key type that cannot be compared to the others are skipped
new_cache.put(1, "Omega")
new_cache.put(True, "Yolo")
new_cache.put(("3", 2), ("Theta", "Beta"))
new_cache.print_cache()
new_cache.put([2, 3], "Epson")
new_cache.put({"d": 4}, "Delta")
new_cache.put(
    {7, 8, 9},
    "Swing and miss, and then again, attentively each time, making adjustment and improvements, bit by bit, massive or small",
)
new_cache.print_cache()


print(my_cache.get("C"))
print(my_cache.get(None))
print(my_cache.get("H"))
