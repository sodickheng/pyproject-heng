# Using the global keyword allows you to "modify" the global variable inside the function:
x = 10  # Global variable

def modify():
    global x  # Tell Python we want to use the global variable x
    x = 20  # Modify the global variable x
    print("Inside modify:", x)  # Output: 20 (global variable)

modify()
print("Outside modify:", x)  # Output: 20 (global variable is changed)
