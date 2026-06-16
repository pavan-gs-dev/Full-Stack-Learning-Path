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

# string (str)
name = "John"           
print(type(name))
print(name)

# Boolean (bool)    
is_active = True    
print(type(is_active))
print(is_active)


# check the size of the data types using sys.getsizeof() function
import sys

print(sys.getsizeof(22))
print(sys.getsizeof(99.99))
print(sys.getsizeof(True))
print(sys.getsizeof("Pavan"))


# =========================
# LIST
# =========================

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

fruits.append("Orange")
print("After Append:", fruits)

fruits.insert(1, "Kiwi")
print("After Insert:", fruits)

fruits.remove("Banana")
print("After Remove:", fruits)

fruits.pop()
print("After Pop:", fruits)

print("Length:", len(fruits))

for fruit in fruits:
    print(fruit)


# =========================
# TUPLE
# =========================

numbers = (10, 20, 30, 40)

print("\nTuple:", numbers)

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

print("Length:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

for num in numbers:
    print(num)


# =========================
# SET
# =========================

data = {1, 2, 3, 4, 5}

print("\nOriginal Set:", data)

data.add(6)
print("After Add:", data)

data.remove(2)
print("After Remove:", data)

duplicate_data = {1, 1, 2, 2, 3, 3}
print("Duplicates Removed:", duplicate_data)

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

print("3 Exists:", 3 in a)


# =========================
# FROZENSET
# =========================

frozen_data = frozenset([1, 2, 3, 4])

print("\nFrozenset:", frozen_data)

print("Length:", len(frozen_data))
print("3 Exists:", 3 in frozen_data)

for item in frozen_data:
    print(item)


# =========================
# DICTIONARY
# =========================

student = {
    "name": "Pavan",
    "age": 22,
    "city": "Bangalore"
}

print("\nDictionary:", student)

print("Name:", student["name"])
print("Age:", student.get("age"))

student["college"] = "ABC College"
print("After Add:", student)

student["age"] = 23
print("After Update:", student)

del student["city"]
print("After Delete:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

for key, value in student.items():
    print(key, ":", value)

