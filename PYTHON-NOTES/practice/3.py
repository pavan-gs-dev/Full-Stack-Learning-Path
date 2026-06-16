# ==========================================================
# PYTHON INPUT, OUTPUT, OPERATORS & TYPE CONVERSION
# Complete Learning Example with Comments
# ==========================================================


# ==========================================================
# INPUT AND OUTPUT
# ==========================================================

# Taking input from user
# input() always returns data as STRING

name = input("Enter your name: ")

print("Your name is:", name)

# Check data type

print("Data Type:", type(name))


# Taking integer input

age = int(input("Enter your age: "))

print("Age:", age)
print("Data Type:", type(age))


# Taking float input

salary = float(input("Enter your salary: "))

print("Salary:", salary)
print("Data Type:", type(salary))


# ==========================================================
# OUTPUT FORMATTING
# ==========================================================

print("\n===== OUTPUT FORMATTING =====")

name = "Pavan"
age = 22

# Normal print

print("Name:", name)

# Multiple values

print("Name:", name, "Age:", age)

# f-string (Most Used)

print(f"My name is {name} and I am {age} years old")


# ==========================================================
# ARITHMETIC OPERATORS
# ==========================================================

print("\n===== ARITHMETIC OPERATORS =====")

a = 10
b = 3

# Addition

print("Addition:", a + b)

# Subtraction

print("Subtraction:", a - b)

# Multiplication

print("Multiplication:", a * b)

# Division

print("Division:", a / b)

# Floor Division

print("Floor Division:", a // b)

# Modulus (Remainder)

print("Modulus:", a % b)

# Power

print("Power:", a ** b)


# ==========================================================
# COMPARISON OPERATORS
# ==========================================================

print("\n===== COMPARISON OPERATORS =====")

x = 10
y = 20

# Equal To

print("x == y:", x == y)

# Not Equal To

print("x != y:", x != y)

# Greater Than

print("x > y:", x > y)

# Less Than

print("x < y:", x < y)

# Greater Than or Equal To

print("x >= y:", x >= y)

# Less Than or Equal To

print("x <= y:", x <= y)


# ==========================================================
# LOGICAL OPERATORS
# ==========================================================

print("\n===== LOGICAL OPERATORS =====")

a = True
b = False

# AND

print("a and b:", a and b)

# OR

print("a or b:", a or b)

# NOT

print("not a:", not a)


# ==========================================================
# ASSIGNMENT OPERATORS
# ==========================================================

print("\n===== ASSIGNMENT OPERATORS =====")

x = 10

print("Original Value:", x)

# Add and Assign

x += 5
print("After += :", x)

# Subtract and Assign

x -= 2
print("After -= :", x)

# Multiply and Assign

x *= 3
print("After *= :", x)

# Divide and Assign

x /= 2
print("After /= :", x)


# ==========================================================
# MEMBERSHIP OPERATORS
# ==========================================================

print("\n===== MEMBERSHIP OPERATORS =====")

fruits = ["Apple", "Banana", "Mango"]

# Check if item exists

print("Apple" in fruits)

# Check if item does not exist

print("Orange" not in fruits)


# ==========================================================
# IDENTITY OPERATORS
# ==========================================================

print("\n===== IDENTITY OPERATORS =====")

list1 = [1, 2, 3]

# list2 points to same object

list2 = list1

# Compare memory address

print("list1 is list2:", list1 is list2)

# Compare memory address

print("list1 is not list2:", list1 is not list2)


# ==========================================================
# BITWISE OPERATORS
# ==========================================================

print("\n===== BITWISE OPERATORS =====")

a = 5      # Binary = 0101
b = 3      # Binary = 0011

# AND

print("a & b =", a & b)

# OR

print("a | b =", a | b)

# XOR

print("a ^ b =", a ^ b)

# NOT

print("~a =", ~a)

# Left Shift

print("a << 1 =", a << 1)

# Right Shift

print("a >> 1 =", a >> 1)


# ==========================================================
# TYPE CONVERSION
# ==========================================================

print("\n===== TYPE CONVERSION =====")


# ----------------------------------------------------------
# STRING TO INTEGER
# ----------------------------------------------------------

num = "100"

converted_num = int(num)

print(converted_num)
print(type(converted_num))


# ----------------------------------------------------------
# INTEGER TO STRING
# ----------------------------------------------------------

age = 22

age_text = str(age)

print(age_text)
print(type(age_text))


# ----------------------------------------------------------
# INTEGER TO FLOAT
# ----------------------------------------------------------

number = 50

float_number = float(number)

print(float_number)
print(type(float_number))


# ----------------------------------------------------------
# FLOAT TO INTEGER
# ----------------------------------------------------------

price = 99.99

integer_price = int(price)

print(integer_price)
print(type(integer_price))


# ----------------------------------------------------------
# STRING TO FLOAT
# ----------------------------------------------------------

salary = "25000.50"

salary_float = float(salary)

print(salary_float)
print(type(salary_float))


# ----------------------------------------------------------
# INTEGER TO BOOLEAN
# ----------------------------------------------------------

value = 1

boolean_value = bool(value)

print(boolean_value)
print(type(boolean_value))


# ----------------------------------------------------------
# BOOLEAN TO INTEGER
# ----------------------------------------------------------

flag = True

integer_flag = int(flag)

print(integer_flag)
print(type(integer_flag))


# ==========================================================
# IMPLICIT TYPE CONVERSION
# ==========================================================

print("\n===== IMPLICIT TYPE CONVERSION =====")

# Python automatically converts int to float

a = 10
b = 5.5

result = a + b

print(result)
print(type(result))


# ==========================================================
# TYPE CHECKING
# ==========================================================

print("\n===== TYPE CHECKING =====")

name = "Pavan"
age = 22
salary = 25000.50
is_student = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))


# ==========================================================
# END OF PROGRAM
# ==========================================================

print("\nPython Fundamentals Completed Successfully!")

