import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'anna',
    user = 'root',
    password = ''
)



mycursor = mydb.cursor(dictionary=True)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Cloth(
        ID INT NOT NULL AUTO_INCREMENT,
        clothname VARCHAR(255),
        tailorname VARCHAR(255),
        design VARCHAR(255),
        size VARCHAR(255),
        price VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)
