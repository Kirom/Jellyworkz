from flask import Flask, render_template
from flask_mysql_connector import MySQL

app = Flask(__name__)

# Configuring database
config = {
    'user': 'user',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'flask_db',
}

# Configuring database
app.config['MYSQL_USER'] = config['user']
app.config['MYSQL_PASSWORD'] = config['password']
app.config['MYSQL_DATABASE'] = config['database']
app.config['MYSQL_HOST'] = config['host']
mysql = MySQL(app)


# route for printing json of all stories related to userId
@app.route('/user/<string:userId>')
def show_stories(userId):
    # Selects stories matching conditions
    stories = f"SELECT user_id, title FROM stories WHERE user_id={userId}"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(stories)
    qs = cur.fetchall()
    return render_template('user_id.html', qs=qs)


# route for printing json of specific story id
@app.route('/story/<id>')
def show_story(id):
    # Selects stories matching conditions
    stories = f"SELECT * FROM stories WHERE id={id}"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(stories)
    qs = cur.fetchall()
    return render_template('id.html', qs=qs)


# route for printing all titles containing the data in the title
@app.route('/title/<title>')
def show_titles(title):
    # Selects titles matching conditions
    titles = f"SELECT title FROM stories WHERE title LIKE '%{title}%'"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(titles)
    qs = cur.fetchall()
    return render_template('title.html', qs=qs)


if __name__ == '__main__':
    app.run()
