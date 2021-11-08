import sqlite3
from properties import CONNECTION


def writePlayerData(playerName: str, playerScore: int, gameMode: str):

    # Database Connection
    connection = sqlite3.connect(CONNECTION)

    cursor = connection.cursor()

    # Game Mode -> Table name
    gameMode = gameMode.lower()

    queryString = (
        "INSERT INTO "
        + gameMode
        + "(player_name, player_score)"
        + " VALUES ("
        + "'"
        + playerName.lower()
        + "'"
        + ", "
        + str(playerScore)
        + ")"
    )

    cursor.execute(queryString)

    connection.commit()

    connection.close()


def getPlayerData(gameMode: str):

    values = []

    # Database Connection
    connection = sqlite3.connect(CONNECTION)

    cursor = connection.cursor()

    # Game Mode -> Table name
    gameMode = gameMode.lower()

    queryString = (
        "SELECT player_name, player_score FROM "
        + gameMode
        + " ORDER BY player_score DESC"
    )

    for row in cursor.execute(queryString):
        values.append(row)

    connection.close()

    return values
