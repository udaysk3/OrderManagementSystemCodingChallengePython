import pyodbc

class DBConnUtil:
    @staticmethod
    def getDBConn():
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                                        'Server=UDAYSK\SQLEXPRESS;'
                                        'Database=PythonCodingChallenge;'
                                        'Trusted_Connection=yes;')
            return connection
        except Exception as e:
            print("Error connecting to database:", e)
            return None