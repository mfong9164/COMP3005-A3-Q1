import app

### EDIT DATABASE CONNECTION INFORMATION HERE ###
DBNAME = 'COMP 3005: A3Q1'
DBUSERNAME = 'postgres'
DBPASSWORD = '1234'
#################################################

def main():
    conn = app.App(DBNAME, DBUSERNAME, DBPASSWORD)
    if conn:
        choice = -1
        while choice != 0:
            print('''
1 - getAllStudents()
2 - addStudent(first_name, last_name, email, enrollment_date)
3 - updateStudentEmail(student_id, new_email)
4 - deleteStudent(student_id)
Else - Exit
            ''')
            choice = int(input('Select an option:'))
            if choice == 1:
                success = conn.getAllStudents()
            elif choice == 2:
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                email = input('Email: ')
                enrollment_date = input('Date (Format: \'YYYY-MM-DD\'): ')
                success = conn.addStudent(first_name, last_name, email, enrollment_date)
            elif choice == 3:
                student_id = input('Student ID: ')
                new_email = input('New Email: ')
                success = conn.updateStudentEmail(student_id, new_email)
            elif choice == 4:
                student_id = input('Student ID: ')
                success = conn.deleteStudent(student_id)
            else:
                success = False
            
            if not success:
                choice = 0
    del conn

if __name__ == '__main__':
    main()