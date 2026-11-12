class DatabaseConnection:
    def __enter__(self):
        print("Database connected")
        return self

    def execute(self, query):
        print("Executing:", query)
        raise ValueError("Query failed")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database disconnected")
        return False


try:
    with DatabaseConnection() as db:
        db.execute("SELECT * FROM users")

except ValueError as error:
    print("Handled:", error)
    
    
#note : just a contextManger code not DB connection code
'''
Here , __exit__ returns false so exception is carried by python and except block catches it but if it returned turn then it suppresses the exception and continuous in normal flow 
'''

