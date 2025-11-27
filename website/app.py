from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database/grocery.db')  # Use your actual DB path
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grocery')
def show_grocery():
    conn = get_db_connection()
    grocery = conn.execute('SELECT * FROM grocery').fetchall()
    conn.close()
    return render_template('search_grocery.html', grocery=grocery)

@app.route('/grocery_table')
def show_grocery_table():
    conn = get_db_connection()
    grocery = conn.execute('SELECT * FROM grocery').fetchall()
    conn.close()
    return render_template('grocery_table.html', grocery=grocery)

#Create new route for search
@app.route('/search')
def search():
    ## For this request work we should from flask import  request too
    query = request.args.get('query', '')  
    conn = get_db_connection()  
    grocery = conn.execute("SELECT * FROM grocery WHERE product_Name LIKE ?", ('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('search_grocery.html', grocery=grocery)

if __name__ == '__main__':
    app.run(debug=True)
