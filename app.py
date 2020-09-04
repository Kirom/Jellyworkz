from flask import Flask, render_template
from flask_mysql_connector import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE'] = 'flask_db'
mysql = MySQL(app)


@app.route('/story/<string:userId>')
def show_stories(userId):
    stories = f"SELECT user_id, title FROM stories WHERE user_id={userId}"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(stories)
    qs = cur.fetchall()
    return render_template('user_id.html', qs=qs)


@app.route('/story/<id>')
def show_story(id):
    stories = f"SELECT * FROM stories WHERE id={id}"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(stories)
    qs = cur.fetchall()
    return render_template('id.html', qs=qs)


@app.route('/title/<title>')
def show_titles(title):
    titles = f"SELECT title FROM stories WHERE title LIKE '%{title}%'"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(titles)
    qs = cur.fetchall()
    return render_template('title.html', qs=qs)


if __name__ == '__main__':
    app.run()
