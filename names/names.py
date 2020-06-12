import time
from binary_search_tree import BSTNode

start_time = time.time()

"""opens this file in 'read' mode only"""
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

"""opens this file in 'read' mode only"""
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""creates array to keep track of duplicates"""
duplicates = []  # Return the list of duplicates in this data structure

"""
-- original solution provided below -- 
The runtime is 6.52 seconds. the runtime complexity of this block of code is quadratic
because it contains a nested for-loop. for every item in name_1, it scans every item in name_2
causing the Big-O notation to be O(n^2)
"""
# # Replace the nested for loops below with your improvementsS
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()

# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print(f"runtime: {end_time - start_time} seconds")

""" 
-- New solution below --
the new runtime is 0.098 seconds. the new runtime complexity is O(n + n) which reduces to O(n)
"""
binary_search_tree = BSTNode("")

for name_1 in names_1:
    binary_search_tree.insert(name_1)

for name_2 in names_2:
    if binary_search_tree.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
