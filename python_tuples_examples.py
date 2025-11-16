
# Tuples in Python - Examples and Explanations

# 1. Creating tuples
t1 = (10, 20, 30)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.14, True)
t4 = 10, 20, 30  # tuple without parentheses
t5 = (10,)       # single element tuple
t6 = ()          # empty tuple
t7 = (1, 2, (3, 4, 5))  # nested tuple

print("Tuples:", t1, t2, t3, t4, t5, t6, t7)

# 2. Accessing elements
print("First element of t2:", t2[0])
print("Last element of t2:", t2[-1])

# 3. Slicing tuples
numbers = (10, 20, 30, 40, 50, 60)
print("Slice numbers[1:4]:", numbers[1:4])
print("Slice numbers[:3]:", numbers[:3])
print("Slice numbers[::2]:", numbers[::2])

# 4. Tuple immutability demonstration
try:
    t1[1] = 50  # This will cause an error
except TypeError as e:
    print("Error:", e)

# 5. Modify tuple indirectly via list
t_list = list(t1)
t_list.append(40)
t1_modified = tuple(t_list)
print("Modified tuple:", t1_modified)

# 6. Tuple methods
t_count = (10, 20, 20, 20, 30)
print("Count of 20:", t_count.count(20))
print("Index of 'banana':", t2.index("banana"))

# 7. Looping through tuple
for fruit in t2:
    print("Fruit:", fruit)

# 8. Tuple packing and unpacking
packed = 10, 20, 30
a, b, c = packed
print("Unpacked values:", a, b, c)

# Extended unpacking
extended = (1, 2, 3, 4, 5)
x, *y, z = extended
print("Extended unpacking:", x, y, z)

# Example program
student = ("John", 21, "CSE", 8.7)
print("Student details:")
print("Name:", student[0])
print("Age:", student[1])
print("Branch:", student[2])
print("CGPA:", student[3])
