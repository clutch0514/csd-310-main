# Ronald Rojas
# CYBR410-T302
# Prof. P. Haas
# 02/12/2023


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root2",
    "password": "password",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}



def show_players(cursor, title):

# Inner Join 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

# Get the results
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
# Display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    db = mysql.connector.connect(**config)

# Get the object 
    cursor = db.cursor()

# Player Query
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

# Player data
    player_data = ("Rubeus", "Hagrid", 1)

# Insert new record
    cursor.execute(add_player, player_data)


    db.commit()

# Show all the records for the player
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

# Update the new record
    update_player = ("UPDATE player SET team_id = 1, first_name = 'Rubeus', last_name = 'Hagrid' WHERE first_name = 'Rubeus'")

    cursor.execute(update_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("DELETE FROM player WHERE first_name = 'Rubeus'")

    cursor.execute(delete_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

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