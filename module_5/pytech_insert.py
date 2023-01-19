# Ronald Rojas
# CYBR410-T302
# Prof. P. Haas
# Module 5 - Assignment 5.3 - Collection Queries - Pytech Insert

# Pymongo Client
from pymongo import MongoClient

# Database URL and db collection
url = "mongodb+srv://admin:admin@cluster0.ylcwehg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech


    #Toby Maguire's document information
toby = {
        "student_id": "1007",
        "first_name": "Toby",
        "last_name": "Maguire"
    },
   #Andrew Garfield's document information
andrew = {
        "student_id": "1008",
        "first_name": "Andrew",
        "last_name": "Garfield"
    },
    #Tom Holland's document information
tom = {
        "student_id": "1009",
        "first_name": "Tom",
        "last_name": "Holland"
    }


students = db.students

# Labels the function of the program on the Output window
print("\n -- INSERT STATEMENTS --")


#Toby
toby_student_id = students.insert_one(toby).inserted_id
print(" Inserted student record Toby Maguire into the students collection with document_id " + str(toby_student_id))


#Andrew
andrew_student_id = students.insert_one(andrew).inserted_id
print(" Inserted student record Andrew Garfield into the students collection with document_id " + str(andrew_student_id))


#Tom
tom_student_id = students.insert_one(tom).inserted_id
print(" Inserted student record Tom Holland into the students collection with document_id " + str(tom_student_id))


input("\n\n End of program, press any key to exit...")