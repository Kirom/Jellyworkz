import requests
import json
import mysql.connector

config = {
    'user': 'user',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'flask_db',
}

cnx = mysql.connector.connect(**config)

with cnx.cursor() as cursor:
    # If table already exists, drop it
    cursor.execute("DROP TABLE IF EXISTS stories;")

with cnx.cursor() as cursor:
    # creates table
    create_table = (
        "CREATE TABLE `stories` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `title` varchar(255) NOT NULL,"
        "  `user_id` varchar(14) NOT NULL,"
        "  PRIMARY KEY (`id`)"
        ")")
    cursor.execute(create_table)

todos = requests.get('https://jsonplaceholder.typicode.com/todos/').text
data = json.loads(todos)

with cnx.cursor() as cursor:
    for todo in data[:100]:
        completed = todo['completed']
        if completed:
            # checks 'comleted' status and if True, then inserting data in db.
            title = todo['title']
            user_id = todo['userId']
            data = {'title': title, 'user_id': user_id}
            add_story = (
                "INSERT INTO stories (title, user_id) VALUES (%(title)s, %(user_id)s);"
            )
            cursor.execute(add_story, data)

cnx.commit()
cnx.close()
