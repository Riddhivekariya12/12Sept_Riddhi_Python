import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_managemnt"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.fetchall()
