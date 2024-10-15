import mysql.connector
from mysql.connector import Error
import os

def create_database():
    try:
        # Retrieve the MySQL password from the environment variable
        password = os.getenv('MYSQL_PASSWORD')

        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',      # Change if your MySQL server is hosted elsewhere
            user='root',           # Replace with your MySQL username
            password=password       # Use the retrieved password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
