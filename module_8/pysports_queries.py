# Ronald Rojas
# CYBR410-T302
# Prof. P. Haas
# 02/10/2023


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "password",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    # Try/catch MySQL database errors 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # Select from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Retrieve the results
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # Display the results in this specific order
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # Select the querie for the player
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # Get the player results
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # Retreive the overall results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
   
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
  db.close()
