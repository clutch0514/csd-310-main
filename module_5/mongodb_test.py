# Ronald Rojas
# CYBR410-T302
# Prof. P. Haas
# Module 5 Assignment 5.2 - PyTech: Collection Creation

# Import necessary extensions
from pymongo import MongoClient
import msvcrt

# Define Values
url = "mongodb+srv://admin:admin@cluster0.ylcwehg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Print messages on screen
print(' -- Pytech C0llection List -- ')
print(db.list_collection_names())

# Print message to press any key to exit
input("End of program, press any key to exit...")
import msvcrt as m
def wait():
    m.getch()




