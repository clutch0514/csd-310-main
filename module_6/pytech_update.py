#Ronald Rojas
# Prof. P. Haas
#CYBR410-T302
#01/21/2023

# PyTech: Updating Documents - Update

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ylcwehg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

# Display the program function step
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print( " Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# Update records on student 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Mac"}})

# Find the updated document
Toby = students.find_one({"student_id": "1007"})

# Display the program function step
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

# Show the update in Output
print("  Student ID: " + Toby["student_id"] + "\n  First Name: " + Toby["first_name"] + "\n  Last Name: " + Toby["last_name"] + "\n")

# Exit 
input("\n\n  End of program, press any key to continue...")