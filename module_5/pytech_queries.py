# Ronald Rojas
# CYBR410-T302
# Prof. P. Haas
# Module 5 - Assignment 5.3 - Collection Queries - Pytech Queries

# Pymongo Client
from pymongo import MongoClient
import msvcrt

# Database URL and db collection
url = "mongodb+srv://admin:admin@cluster0.ylcwehg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students

student_list = students.find({})

# Labels the function of the program on the Output window
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Browse the collection and output the results of find()
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Find document
Andrew = students.find_one({"student_id": "1008"})

# Output the results from find one
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + Andrew["student_id"] + "\n  First Name: " + Andrew["first_name"] + "\n  Last Name: " + Andrew["last_name"] + "\n")

# Display exit prompt 
input("\n\n  End of program, press any key to continue...")