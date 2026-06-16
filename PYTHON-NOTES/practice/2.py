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
  
#   ======================
#   DATA TYPES 


# Integer (int)
x = 999999999999999999999999999999999999999999
age = 22
print(type(age))
print(x)


# Float (float)
y = 3.14        
print(type(y))

# complex (complex)
z = 2 + 3j
print(type(z))
print(z)

a = 3 + 4j
b = 2 + 5j

print(a * b)
x = 3 + 4j

print(x.real)
print(x.imag)