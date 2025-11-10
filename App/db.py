import psycopg2

# Connects to a localhost Database based on the inputted values
# @param {string} dbName - Name of Database
# @param {string} usr - User's Name
# @param {string} pwd - User's Password
# @return {connection} conn
def connect(dbName, usr, pwd):
    try:
        conn = psycopg2.connect(
            dbname=dbName,
            user=usr,
            password=pwd, 
            host='localhost'
        )
        conn.autocommit = True
        return conn
    except Exception as e:
        print(e)
        return None

# Disconnect if connection found
# @param {connection} conn
def disconnect(conn):
    if conn:
        conn.close()

# Execute SQL statements
# @param {connection} conn
# @param {string} statement
# @param {(string)} params
# @return {bool, array} success?, result
def execute(conn, statement, params):
    with conn.cursor() as curs:
        try:
            curs.execute(statement, params)
            if statement.lower().startswith('select'):
                result = curs.fetchall()
            else:
                result = None
            return True, result
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False, None