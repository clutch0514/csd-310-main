#Ronald Rojas
# Prof. P. Haas
#CYBR410-T302
#01/21/2023

# PyTech: Updating Documents - Delete

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ylcwehg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

#Display the purpose of the program
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print( " Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")


test_doc = {
    "student_id": "1010",
    "first_name": "Eddy",
    "last_name": "Brock"
}

test_doc_id = students.insert_one(test_doc).inserted_id

# Display the program function step
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# Call the find_one() method
student_test_doc = students.find_one({"student_id": "1010"})

# Display the program function step
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# Call the delete_one method to remove the student.
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# fFind all the students
new_student_list = students.find({})

# Display the program function step
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")