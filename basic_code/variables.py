# Python Variables 
""" 1. What is a Variable?
A variable is a name that stores a value in memory.
You can think of it like a label on a box that holds some data.

2. Rules for Naming Variables

✅ Can contain letters, digits, and underscores (_)
✅ Must start with a letter or underscore, not a number
✅ Case-sensitive (age,Age and AGE are different)
✅ Should not use Python keywords (like if, for, class, etc.)



"""

# variables are case-sensitive
age = 24
Age = 25
AGE = 26

# Valid: Vars
count = 100
user_name = "Reddy"
_age = 25

############## Invalid Vars ##################################

# 2name = "Divakar"   # ❌ starts with number
# user-name = "Reddy" # ❌ contains hyphen
# class = "BCA"       # ❌ 'class' is a keyword
#############################################################

"""
3. Dynamic Typing

Python is dynamically typed — you don’t need to declare a variable type.
Type is decided at runtime based on the assigned value.
"""

x = 10       # int
x = "Hello"  # now it's a str
x = 3.14     # now it's a float

# we can get thetype of variable using type() function
name = 'Divakar'
print(type(age))
print(type(name))

# Variables can change their type after that have been set
name = 899
print(type(name)) ## type will be str now after name is been set with 899


# Assign multiple values to multiple variables

a,b,c = "India","China","Brazil"
print(a)
print(b)
print(c)

# Assign one value to multiple variables
x=y=z = 99
print(x)
print(y)
print(z)


"""
4. Variable Types (Basic Examples)

Python has several data types you can store in variables:
"""

num = 42             # int
pi = 3.14159         # float
name = "Python"      # str
is_valid = True      # bool
fruits = ["apple", "banana", "cherry"]  # list
person = {"name": "Divakar", "age": 30} # dict

"""
5. Best Practices

✅ Use meaningful names (total_sales, not ts)
✅ Follow snake_case naming style
✅ Avoid overwriting built-in names like list, dict, sum, etc.
✅ Use constants for fixed values 
"""