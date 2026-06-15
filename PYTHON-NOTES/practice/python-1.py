a = 10
print(a)  # Output: 10
b = a
print(b)  # Output: 10
a = 20
print(a)  # Output: 20
print(b)  # Output: 10

# Local Variable

def show():
    x = 10

# Global Variable
x = 10

def show():
    print(x)    

x = 10
print(id(x))    