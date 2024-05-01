import mysql.connector

# CREATE TABLE users(name VARCHAR(20), age INT);
# INSERT INTO users VALUES('kamala',24), ('nayana',23),('gamya',29);
# SELECT * FROM users WHERE age = 29
# DELETE FROM users WHERE age > 24
# SELECT * FROM users;
query = "UPDATE users SET age=26 WHERE name='nayana' "

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='connector',
        user='root',
        password='Gaya39877@',
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(query)
        print("run successfully.")


        # result = cursor.fetchall()
        # print(result)

        connection.commit()

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
