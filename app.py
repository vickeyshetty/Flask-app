from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# PostgreSQL database configuration
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'


def connect_to_database():
    """Establishes a connection to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")


@app.route('/')
def index():
    # Connect to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Execute a sample query
        cursor.execute("SELECT * FROM mytable")
        results = cursor.fetchall()

        # Close the database connection
        cursor.close()
        connection.close()

        return render_template('index.html', results=results)
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        return "An error occurred."


if __name__ == '__main__':
    app.run(debug=True)
