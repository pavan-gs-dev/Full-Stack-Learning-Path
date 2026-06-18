
# ==========================================================
# 6.py - PYTHON FILE HANDLING & JSON COMPLETE EXAMPLES
# Topics:
# 1. Create File
# 2. Write File
# 3. Read File
# 4. Read Specific Characters
# 5. Read Line
# 6. Read Lines
# 7. Append File
# 8. File Exists Check
# 9. Delete File
# 10. With Statement
# 11. JSON Basics
# 12. JSON dump()
# 13. JSON load()
# 14. JSON dumps()
# 15. JSON loads()
# ==========================================================

import json
import os


# ==========================================================
# CREATE FILE USING WRITE MODE
# ==========================================================

print("\n===== CREATE FILE =====")

file = open("data.txt", "w")

file.write("Hello Python\n")
file.write("Welcome To File Handling\n")
file.write("Learning Python\n")

file.close()

print("File Created Successfully")


# ==========================================================
# READ ENTIRE FILE
# ==========================================================

print("\n===== READ ENTIRE FILE =====")

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


# ==========================================================
# READ FIRST 5 CHARACTERS
# ==========================================================

print("\n===== READ FIRST 5 CHARACTERS =====")

file = open("data.txt", "r")

print(file.read(5))

file.close()


# ==========================================================
# READ ONE LINE
# ==========================================================

print("\n===== READ ONE LINE =====")

file = open("data.txt", "r")

print(file.readline())

file.close()


# ==========================================================
# READ ALL LINES
# ==========================================================

print("\n===== READ ALL LINES =====")

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ==========================================================
# LOOP THROUGH FILE
# ==========================================================

print("\n===== LOOP THROUGH FILE =====")

file = open("data.txt", "r")

for line in file:
    print(line.strip())

file.close()


# ==========================================================
# APPEND DATA
# ==========================================================

print("\n===== APPEND DATA =====")

file = open("data.txt", "a")

file.write("Appended Line 1\n")
file.write("Appended Line 2\n")

file.close()

print("Data Appended Successfully")


# ==========================================================
# READ AFTER APPEND
# ==========================================================

print("\n===== READ AFTER APPEND =====")

file = open("data.txt", "r")

print(file.read())

file.close()


# ==========================================================
# USING WITH STATEMENT
# ==========================================================

print("\n===== WITH STATEMENT =====")

with open("data.txt", "r") as file:

    print(file.read())


# ==========================================================
# WRITE MULTIPLE LINES
# ==========================================================

print("\n===== WRITE MULTIPLE LINES =====")

with open("students.txt", "w") as file:

    file.write("Pavan\n")
    file.write("Rahul\n")
    file.write("Arjun\n")

print("students.txt Created")


# ==========================================================
# CHECK FILE EXISTS
# ==========================================================

print("\n===== CHECK FILE EXISTS =====")

if os.path.exists("students.txt"):

    print("students.txt Found")

else:

    print("students.txt Not Found")


# ==========================================================
# CREATE FILE USING X MODE
# ==========================================================

print("\n===== CREATE FILE USING X =====")

try:

    file = open("newfile.txt", "x")

    file.close()

    print("newfile.txt Created")

except FileExistsError:

    print("File Already Exists")


# ==========================================================
# FILE INFORMATION
# ==========================================================

print("\n===== FILE INFORMATION =====")

if os.path.exists("data.txt"):

    print("File Size:", os.path.getsize("data.txt"), "bytes")


# ==========================================================
# JSON BASICS
# ==========================================================

print("\n===== PYTHON DICTIONARY =====")

student = {

    "name": "Pavan",
    "age": 22,
    "city": "Bangalore",
    "skills": [
        "Python",
        "SQL",
        "Flutter"
    ]
}

print(student)


# ==========================================================
# DICTIONARY TO JSON STRING
# json.dumps()
# ==========================================================

print("\n===== json.dumps() =====")

json_string = json.dumps(student)

print(json_string)

print(type(json_string))


# ==========================================================
# PRETTY JSON
# ==========================================================

print("\n===== PRETTY JSON =====")

pretty_json = json.dumps(

    student,

    indent=4

)

print(pretty_json)


# ==========================================================
# JSON STRING TO PYTHON OBJECT
# json.loads()
# ==========================================================

print("\n===== json.loads() =====")

json_data = '''
{
    "name":"Pavan",
    "age":22
}
'''

python_object = json.loads(json_data)

print(python_object)

print(type(python_object))


# ==========================================================
# SAVE JSON FILE
# json.dump()
# ==========================================================

print("\n===== json.dump() =====")

with open(

    "student.json",

    "w"

) as file:

    json.dump(

        student,

        file,

        indent=4

    )

print("student.json Saved")


# ==========================================================
# READ JSON FILE
# json.load()
# ==========================================================

print("\n===== json.load() =====")

with open(

    "student.json",

    "r"

) as file:

    data = json.load(file)

print(data)

print(type(data))


# ==========================================================
# ACCESS JSON DATA
# ==========================================================

print("\n===== ACCESS JSON DATA =====")

print(data["name"])

print(data["age"])

print(data["skills"])


# ==========================================================
# LOOP JSON OBJECT
# ==========================================================

print("\n===== LOOP JSON DATA =====")

for key, value in data.items():

    print(key, ":", value)


# ==========================================================
# STORE MULTIPLE STUDENTS
# ==========================================================

print("\n===== MULTIPLE JSON RECORDS =====")

students = [

    {
        "id": 1,
        "name": "Pavan"
    },

    {
        "id": 2,
        "name": "Rahul"
    },

    {
        "id": 3,
        "name": "Arjun"
    }

]

with open(

    "students.json",

    "w"

) as file:

    json.dump(

        students,

        file,

        indent=4

    )

print("students.json Created")


# ==========================================================
# READ MULTIPLE STUDENTS
# ==========================================================

print("\n===== READ STUDENTS JSON =====")

with open(

    "students.json",

    "r"

) as file:

    students_data = json.load(file)

for student in students_data:

    print(student)


# ==========================================================
# UPDATE JSON DATA
# ==========================================================

print("\n===== UPDATE JSON =====")

with open(

    "student.json",

    "r"

) as file:

    student_data = json.load(file)

student_data["salary"] = 50000

with open(

    "student.json",

    "w"

) as file:

    json.dump(

        student_data,

        file,

        indent=4

    )

print("Salary Added")


# ==========================================================
# READ UPDATED JSON
# ==========================================================

print("\n===== UPDATED JSON =====")

with open(

    "student.json",

    "r"

) as file:

    updated_data = json.load(file)

print(updated_data)


# ==========================================================
# DELETE FILE
# ==========================================================

print("\n===== DELETE FILE =====")

if os.path.exists("delete_me.txt"):

    os.remove("delete_me.txt")

    print("File Deleted")

else:

    print("delete_me.txt Not Found")


# ==========================================================
# FILE MODES DEMO
# ==========================================================

print("\n===== FILE MODES =====")

print("r  -> Read")
print("w  -> Write")
print("a  -> Append")
print("x  -> Create")
print("rb -> Read Binary")
print("wb -> Write Binary")


# ==========================================================
# BINARY FILE EXAMPLE
# ==========================================================

print("\n===== BINARY FILE =====")

with open(

    "binary.bin",

    "wb"

) as file:

    file.write(

        b"Hello Binary"

    )

print("Binary File Created")


with open(

    "binary.bin",

    "rb"

) as file:

    data = file.read()

print(data)


# ==========================================================
# END
# ==========================================================

print("\nFile Handling & JSON Examples Completed Successfully!")

