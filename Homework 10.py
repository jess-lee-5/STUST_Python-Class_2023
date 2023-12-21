import sys
import json
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget, QTextBrowser, QMessageBox
from PyQt6.QtCore import Qt
from openpyxl import Workbook

class Student:
    def __init__(self, student_id, name, connection):
        self.student_id = student_id
        self.name = name
        self.courses = {}
        self.connection = connection

    def student_exists(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students WHERE student_id=?", (student_id,))
        return cursor.fetchone()[0] > 0

    def query_course_info(self, semester):
        if semester in self.courses:
            courses_in_semester = self.courses[semester]
            return f"Courses taken by {self.name} in {semester}:", courses_in_semester
        else:
            return f"No courses found for {self.name} in semester {semester}.", None

    def add_course(self, course_code, course_name, semester):
        if semester not in self.courses:
            self.courses[semester] = []

        # Check if the course already exists for the specified semester
        if any(course["code"] == course_code for course in self.courses[semester]):
            return "Course already added for the specified semester."

        self.courses[semester].append({"code": course_code, "name": course_name})

        # Save student information to the database using INSERT OR REPLACE
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO students (student_id, name) VALUES (?, ?)",
                       (self.student_id, self.name))

        # Save the course information to the database
        for course in self.courses[semester]:
            cursor.execute("INSERT OR REPLACE INTO courses (student_id, semester, course_code, course_name) VALUES (?, ?, ?, ?)",
                           (self.student_id, semester, course["code"], course["name"]))

        self.connection.commit()

        return "Course added successfully."

    def get_all_courses_info(self):
        all_courses_info = []
        for semester, courses in self.courses.items():
            for course in courses:
                all_courses_info.append({
                    "student_id": self.student_id,
                    "name": self.name,
                    "semester": semester,
                    "course_code": course["code"],
                    "course_name": course["name"]
                })
        return all_courses_info


    def save_courses_to_database(self, semester):
        cursor = self.connection.cursor()

        # Delete existing course information for the specified semester
        cursor.execute("DELETE FROM courses WHERE student_id=? AND semester=?", (self.student_id, semester))

        # Insert or replace the updated course information for the specified semester
        for course in self.courses[semester]:
            cursor.execute("INSERT OR REPLACE INTO courses (student_id, semester, course_code, course_name) VALUES (?, ?, ?, ?)",
                           (self.student_id, semester, course["code"], course["name"]))

        self.connection.commit()

    def save_to_database(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (self.student_id, self.name))

        for semester, courses in self.courses.items():
            for course in courses:
                cursor.execute("INSERT INTO courses (student_id, semester, course_code, course_name) VALUES (?, ?, ?, ?)",
                               (self.student_id, semester, course["code"], course["name"]))

        self.connection.commit()

    def load_from_database(self):
        cursor = self.connection.cursor()

        # Load student information
        cursor.execute("SELECT * FROM students WHERE student_id=?", (self.student_id,))
        student_data = cursor.fetchone()
        if student_data:
            self.name = student_data[1]

        # Load courses information
        cursor.execute("SELECT * FROM courses WHERE student_id=?", (self.student_id,))
        courses_data = cursor.fetchall()
        for course_data in courses_data:
            semester = course_data[1]
            course_code = course_data[2]
            course_name = course_data[3]
            self.add_course(course_code, course_name, semester)

    def create_tables(connection):
        cursor = connection.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS students (
                       student_id TEXT PRIMARY KEY,
                       name TEXT
                       )
                       ''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS courses (
                       student_id TEXT,
                       semester TEXT,
                       course_code TEXT,
                       course_name TEXT,
                       PRIMARY KEY (student_id, semester, course_code),
                       FOREIGN KEY (student_id) REFERENCES students (student_id)
                       )
                       ''')
        connection.commit()
        
    def generate_sample_data(connection):
        sample_students = []
        for i in range(10):
            student_id = f"STUST{i+1:03d}"
            name = f"Student{i+1}"
            student = Student(student_id, name, connection)
            for course_code, course_name in [("Python", "Python Programming"), ("Java", "Java Programming"),
                                             ("C++", "C++ Programming"), ("JavaScript", "JavaScript Programming"),
                                             ("Database", "Database Management"), ("OS", "Operating Systems")]:
                 semester = "Fall 2023"
                 student.add_course(course_code, course_name, semester)
                 
                 #student.save_to_database()
                 sample_students.append(student)
                 return sample_students

class StudentGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('students.db')

        # Check if the students table exists in the database
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
        table_exists = cursor.fetchone() is not None

        if not table_exists:
            create_tables(self.connection)
            self.generate_sample_data()
            self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()

        self.add_course_tab = self.create_add_course_tab()
        self.query_course_tab = self.create_query_course_tab()
        self.display_all_tab = self.create_display_all_tab()

        self.tabs.addTab(self.add_course_tab, "Add Course")
        self.tabs.addTab(self.query_course_tab, "Query Course")
        self.tabs.addTab(self.display_all_tab, "Display All Students")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('STUST Student Information and Course Query Tool')
    
    def student_exists(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students WHERE student_id=?", (student_id,))
        return cursor.fetchone()[0] > 0
    
    def create_add_course_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.student_id_label_add = QLabel('Student ID:')
        self.student_id_edit_add = QLineEdit()
        self.name_label_add = QLabel('Name:')
        self.name_edit_add = QLineEdit()

        self.course_code_label_add = QLabel('Course Code:')
        self.course_code_edit_add = QLineEdit()
        self.course_name_label_add = QLabel('Course Name:')
        self.course_name_edit_add = QLineEdit()
        self.add_course_button_add = QPushButton('Add Course')

        self.add_course_button_add.clicked.connect(self.add_course)

        layout.addWidget(self.student_id_label_add)
        layout.addWidget(self.student_id_edit_add)
        layout.addWidget(self.name_label_add)
        layout.addWidget(self.name_edit_add)
        layout.addWidget(self.course_code_label_add)
        layout.addWidget(self.course_code_edit_add)
        layout.addWidget(self.course_name_label_add)
        layout.addWidget(self.course_name_edit_add)
        layout.addWidget(self.add_course_button_add)

        tab.setLayout(layout)
        return tab

    def create_add_course_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.student_id_label_add = QLabel('Student ID:')
        self.student_id_edit_add = QLineEdit()
        self.course_code_label_add = QLabel('Course Code:')
        self.course_code_edit_add = QLineEdit()
        self.course_name_label_add = QLabel('Course Name:')
        self.course_name_edit_add = QLineEdit()
        self.semester_label_add = QLabel('Semester:')
        self.semester_edit_add = QLineEdit()

        self.add_course_button_add = QPushButton('Add Course')

        self.add_course_button_add.clicked.connect(self.add_course)

        layout.addWidget(self.student_id_label_add)
        layout.addWidget(self.student_id_edit_add)
        layout.addWidget(self.course_code_label_add)
        layout.addWidget(self.course_code_edit_add)
        layout.addWidget(self.course_name_label_add)
        layout.addWidget(self.course_name_edit_add)
        layout.addWidget(self.semester_label_add)
        layout.addWidget(self.semester_edit_add)
        layout.addWidget(self.add_course_button_add)

        tab.setLayout(layout)
        return tab

    def add_course(self):
        student_id = self.student_id_edit_add.text()
        course_code = self.course_code_edit_add.text()
        course_name = self.course_name_edit_add.text()
        semester = self.semester_edit_add.text()

        # Check for missing input data
        if not student_id or not course_code or not course_name or not semester:
            self.show_alert("Missing Data", "Please fill in all fields.")
            return

        # Check if the student ID exists in the database
        if not self.student_exists(student_id):
            self.show_alert("Invalid Student ID", "Student ID does not exist.")
            return

        # Create or load student profile
        student = Student(student_id, "", self.connection)
        student.load_from_database()

        # Check if the course is already added for the specified semester
        if self.course_exists_for_semester(student, course_code, semester):
            self.show_alert("Course Already Added", "The course is already added for the specified semester.")
            return

        # Add course to the student's profile
        student.add_course(course_code, course_name, semester)

        # Save student course information to the database
        student.save_courses_to_database(semester)

        # Show success message box
        self.show_success_message("Course Added", "The course has been successfully added.")

    def course_exists_for_semester(self, student, course_code, semester):
        return semester in student.courses and any(course["code"] == course_code for course in student.courses[semester])

    def create_query_course_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.student_id_label_query = QLabel('Student ID:')
        self.student_id_edit_query = QLineEdit()
        self.semester_label_query = QLabel('Semester:')
        self.semester_edit_query = QLineEdit()
        self.query_button_query = QPushButton('Query Courses')
        self.result_browser_query = QTextBrowser()

        self.query_button_query.clicked.connect(self.query_courses)

        layout.addWidget(self.student_id_label_query)
        layout.addWidget(self.student_id_edit_query)
        layout.addWidget(self.semester_label_query)
        layout.addWidget(self.semester_edit_query)
        layout.addWidget(self.query_button_query)
        layout.addWidget(self.result_browser_query)

        tab.setLayout(layout)
        return tab

    def query_courses(self):
        student_id = self.student_id_edit_query.text()
        semester = self.semester_edit_query.text()

        # Check for missing input data
        if not student_id or not semester:
            self.show_alert("Missing Data", "Please fill in all fields.")
            return

        # Check if the student ID exists in the database
        if not self.student_exists(student_id):
            self.show_alert("Invalid Student ID", "Student ID does not exist.")
            return

        # Create or load student profile
        student = Student(student_id, "", self.connection)
        student.load_from_database()

        # Query course information
        result_message, courses_info = student.query_course_info(semester)

        # Display result in the QTextBrowser
        self.result_browser_query.setPlainText(result_message)
        if courses_info:
            for course in courses_info:
                self.result_browser_query.append(f"{course['code']}: {course['name']}")


    def create_display_all_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.query_button_display_all = QPushButton('Display All Students')
        self.result_browser_display_all = QTextBrowser()

        self.query_button_display_all.clicked.connect(self.display_all_students)

        layout.addWidget(self.query_button_display_all)
        layout.addWidget(self.result_browser_display_all)

        tab.setLayout(layout)
        return tab

    
    def query_courses(self):
        student_id = self.student_id_edit_query.text()
        semester = self.semester_edit_query.text()

        # Check for missing input data
        if not student_id or not semester:
            self.show_alert("Missing Data", "Please fill in all fields.")
            return

        # Create or load student profile
        student = Student(student_id, "", self.connection)
        student.load_from_database()

        # Query course information
        result_message, courses_info = student.query_course_info(semester)

        # Display result in the QTextBrowser
        self.result_browser_query.setPlainText(result_message)
        if courses_info:
            for course in courses_info:
                self.result_browser_query.append(f"{course['code']}: {course['name']}")

    def display_all_students(self):
        # Generate sample data for at least 10 students at STUST
        sample_students = generate_sample_data(self.connection)

        # Display all student course info in the QTextBrowser
        self.result_browser_display_all.clear()
        for student in sample_students:
            courses_info = student.get_all_courses_info()
            for info in courses_info:
                self.result_browser_display_all.append(f"{info['student_id']} - {info['name']}:")
                self.result_browser_display_all.append(f"  Semester: {info['semester']}")
                self.result_browser_display_all.append(f"  {info['course_code']}: {info['course_name']}")

    def show_alert(self, title, message):
        alert = QMessageBox()
        alert.setWindowTitle(title)
        alert.setText(message)
        alert.exec()

    def show_success_message(self, title, message):
        success_message = QMessageBox()
        success_message.setWindowTitle(title)
        success_message.setText(message)
        success_message.exec()
        
    def main():
        app = QApplication(sys.argv)
        gui = StudentGUI()
        gui.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    main()