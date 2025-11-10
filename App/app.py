import db

# Use App class to store connection throughout application, so that when the function is called, the connection doesn't have to be provided every time
class App:
    # Call db to try to connect to Database. If successful, then Initialize to Assignment Specifications
    # @param {string} dbName - Database Name
    # @param {string} usr - Database User Name
    # @param {string} pwd - Database User Password
    def __init__(self, dbName, usr, pwd):
        conn = db.connect(dbName, usr, pwd)
        if not conn:
            return
        self._conn = conn
        self._initStudentsTable()

    # Initialize students Table to Assignment Specifications
    def _initStudentsTable(self):
        db.execute(self._conn, 'DROP TABLE IF EXISTS students', None)
        db.execute(self._conn, '''
        CREATE TABLE IF NOT EXISTS students(
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        );''', None)
        self.addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
        self.addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
        self.addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

    # Call db to attempt to disconnect from Database
    def __del__(self):
        db.disconnect(self._conn)
        print('Disconnected Successfully')

    # Retrieves and displays all records from the students table.
    def getAllStudents(self):
        statement = 'SELECT * FROM students ORDER BY student_id;'
        success, result = db.execute(self._conn, statement, None)
        if success:
            for row in result:
                print(row)
        return success

    # Inserts a new student record into the students table.
    # @param {string} first_name
    # @param {string} last_name
    # @param {string} email
    # @param {string} enrollment_date - This should follow the SQL Date format, but as a string
    def addStudent(self, first_name, last_name, email, enrollment_date):
        statement = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);'
        params = (first_name, last_name, email, enrollment_date)
        success, result = db.execute(self._conn, statement, params)
        return success
    
    # Updates the email address for a student with the specified student_id.
    # @param {string} student_id
    # @param {string} new_email
    def updateStudentEmail(self, student_id, new_email):
        statement = 'UPDATE students SET email = %s WHERE student_id = %s;'
        params = (new_email, student_id)
        success, result = db.execute(self._conn, statement, params)
        return success
    
    # Deletes the record of the student with the specified student_id.
    # @param {string} student_id
    def deleteStudent(self, student_id):
        statement = 'DELETE FROM students WHERE student_id = %s;'
        params = (student_id)
        success, result = db.execute(self._conn, statement, params)
        return success