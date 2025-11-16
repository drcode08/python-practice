"""
🌍 1. What is a Variable’s Scope?

The scope of a variable is the region of code where it can be accessed.
Python has two main types of variable scope:
Local variables → defined inside a function
Global variables → defined outside all functions

🧠 2. Global Variables

A global variable is declared outside any function and can be accessed anywhere in the code.

"""

# ✅ Global variables can be read from inside functions.

x = 99  # Global variable

def display():
    print("Inside function:", x)  # Access global variable

display()
print("Outside function:", x)

x = 100 # Global Variable
def display():
    x = "Hello! Divakar" # Local variable
    print("Inside the function ",x) # Access local variable

display()
print("Outside the Function",x)

"""
🧩 3. Local Variables

A local variable is declared inside a function, and it exists only inside that function.
"""

def greet():
    message = "Hello, Divakar!"  # Local variable
    print(message)

greet()
# print(message)  # ❌ Error: message is not defined


"""
⚠️ 4. Modifying Global Variables Inside a Function

If you want to change a global variable inside a function, you must use the global keyword.
"""

x ='India'
def greet():
    global x
    x = 'Bharath'
    print("Country Name changed to ", x)

greet()
print(x)


## Update the count 
count = 10

def update_count():
    global count
    count = count + 5  # modifies global variable

update_count()
print("Updated count:", count)

"""
🧩 5. Local vs Global Variable Example

When a variable with the same name exists in both local and global scopes:
"""

# Local variable overrides the global one only inside the function.

x = 50 # Global variable

def test():
    x = 25 # Local variable (same name)
    print("Inside Function: ", x)

test()
print("Outside Function: ", x)

"""
6. Using globals() Function

You can access or modify a global variable using the built-in globals() function.
"""

x = 5

def modify():
    globals()['x'] = 20

modify()
print("x =", x)

"""
Summary :

| Type   | Declared         | Accessible Where     | Modified With                   |
| ------ | ---------------- | -------------------- | ------------------------------- |
| Global | Outside function | Everywhere           | `global` keyword or `globals()` |
| Local  | Inside function  | Only within function | Not applicable                  |


"""