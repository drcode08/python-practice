# Python Sets Examples

# 1. Creating sets
s1 = {1, 2, 3}
s2 = {1, 2, 2, 3, 3}
print("Set with duplicates removed:", s2)

# 2. Empty set
empty_set = set()
print("Empty set:", empty_set)

# 3. Adding elements
s = {10, 20, 30}
s.add(40)
s.update([50, 60])
print("After adding elements:", s)

# 4. Removing elements
s.remove(20)
s.discard(100)  # No error even if not present
removed_item = s.pop()  # Removes random item
print("After removals:", s)
print("Randomly removed:", removed_item)

# 5. Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric difference:", a ^ b)

# 6. Relations
print("Is subset:", {1,2}.issubset({1,2,3}))
print("Is superset:", {1,2,3}.issuperset({2}))
print("Is disjoint:", {1,2}.isdisjoint({3,4}))

# 7. Frozen set
fs = frozenset({1, 2, 3})
print("Frozen set:", fs)
