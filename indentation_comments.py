# Let's create a Python file with detailed explanation and examples about Indentation.


# Python Indentation Examples and Explanation

# Indentation is how Python defines code blocks. It uses spaces (usually 4 per level) instead of curly braces.

# ---------------------------
# 1. Basic Indentation Example
# ---------------------------

if True:
    print("Indented line runs because condition is True")
print("This line is outside the if block")

# ---------------------------
# 2. Function Indentation
# ---------------------------

def greet(name):
    if name:
        print("Hello,", name)
    else:
        print("Hello, stranger!")

greet("Divakar")
greet("")

# ---------------------------
# 3. Loop Indentation
# ---------------------------

for i in range(3):
    print("Iteration:", i)
    if i == 1:
        print("  Inner block under if inside for loop")

print("Loop completed")

# ---------------------------
# 4. Nested Blocks Example
# ---------------------------

x = 10
if x > 5:
    print("x is greater than 5")
    if x < 15:
        print("x is also less than 15")
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
print("Done checking x")

# ---------------------------
# 5. Incorrect Indentation Example
# ---------------------------
# The below code will cause an error if uncommented:
#
# if True:
# print("This will raise an IndentationError")
#
# IndentationError: expected an indented block
#
# Always indent using 4 spaces after statements like if, for, while, def, class, etc.

# ---------------------------
# 6. Best Practices
# ---------------------------
# ✅ Use 4 spaces per indentation level.
# ✅ Configure your editor to replace Tab with 4 spaces.
# ✅ Keep all code in a block at the same indentation level.
# ✅ Use code formatters like 'black' or 'autopep8' for consistent indentation.

#################### Python Comments #############

#🧩 1. Single-line Comments

# Start with a hash symbol (#) — everything after # on that line is ignored.

# This is a single-line comment
print("Hello, World!")  # This is an inline comment

# 🧱 2. Multi-line Comments (Block Comments)
# Python doesn’t have a special multi-line comment syntax like other languages.Instead, you can write multiple # lines:

# This is a multi-line comment
# describing the next piece of code.
# It prints a greeting to the user.
print("Hi there!")

# 🧾 3. DocStrings (for documentation)
# If you want to describe a function, class, or module, use triple quotes (""" """ or ''' ''').
#These are called docstrings and are part of the object’s documentation.

def greet(name):
    """
    This function greets the user by name.
    Args:
        name (str): The name of the user
    Returns:
        None
    """
    print("Hello,", name)

greet("Divakar")

# You can access this documentation later using:
print(greet.__doc__)

# 4. Best Practices

#Keep comments short and relevant.
#Update comments when changing code.
#Use docstrings for functions, classes, and modules.
#Avoid obvious comments: