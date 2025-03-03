set_01 = {99, 88, 77, 66, 55, 44}
set_02 = {11, 22, 33, 44, 55, 66}

# Union of two set
union_set = set_01.union(set_02)
print(f"Item in union_set = {union_set}")

# Intersection of two sets
intersection_set = set_01.intersection(set_02)
print(f"Item in intersection_set = {intersection_set}")

# Difference of two sets
difference_set_01 = set_01.difference(set_02)
print(f"Item in difference_set_01 = {difference_set_01}")

difference_set_02 = set_02.difference(set_01)
print(f"Item in difference_set_02 = {difference_set_02}")

# Checking for subset
is_subset = set_01.issubset(set_02)
print(f"set_01 is a subset of set_02 = {is_subset}")
