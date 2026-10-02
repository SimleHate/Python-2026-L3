#Practical_Work_2
# File: 2.student.mark.oop.py

class Student:
    def __init__(self):
        # Tính đóng gói (Encapsulation): Sử dụng dấu __ để biến thuộc tính thành private
        self.__id = ""
        self.__name = ""
        self.__dob = ""

    # Tính đa hình (Polymorphism): Phương thức .input() cho sinh viên
    def input(self):
        self.__id = input("  Student ID: ")
        self.__name = input("  Student Name: ")
        self.__dob = input("  DoB (dd/mm/yyyy): ")

    # Tính đa hình (Polymorphism): Phương thức .list() cho sinh viên
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")

    # Getters để truy xuất dữ liệu an toàn
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    # Tính đa hình (Polymorphism): Phương thức .input() cho môn học (Cùng tên, khác luồng thực thi)
    def input(self):
        self.__id = input("  Course ID: ")
        self.__name = input("  Course Name: ")

    # Tính đa hình (Polymorphism): Phương thức .list() cho môn học
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name}")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {} # Lưu trữ dạng { course_id: { student_id: mark } }

    def add_students(self):
        n = int(input("Enter number of students in the class: "))
        print(f"\n--- Entering information for {n} student(s) ---")
        for i in range(n):
            print(f"Student {i+1}:")
            s = Student()
            s.input() # Gọi phương thức input() của đối tượng Student
            self.__students.append(s)

    def add_courses(self):
        n = int(input("\nEnter number of courses: "))
        print(f"\n--- Entering information for {n} course(s) ---")
        for i in range(n):
            print(f"Course {i+1}:")
            c = Course()
            c.input() # Gọi phương thức input() của đối tượng Course
            self.__courses.append(c)
            self.__marks[c.get_id()] = {} # Chuẩn bị dict lưu điểm cho môn học

    def input_marks(self):
        print("\n--- Input Marks ---")
        cid = input("Enter course id for mark: ")

        # Tìm môn học theo ID
        course = None
        for c in self.__courses:
            if c.get_id() == cid:
                course = c
                break

        if course:
            print(f"Entering marks for course: {course.get_name()}")
            for s in self.__students:
                mark = float(input(f"  Mark for {s.get_name()} (ID: {s.get_id()}): "))
                self.__marks[cid][s.get_id()] = mark
        else:
            print("Invalid course id!")

    def list_students(self):
        print("\n=== LIST OF STUDENTS ===")
        for s in self.__students:
            s.list() # Đa hình: chỉ cần gọi .list(), đối tượng sẽ tự biết cách in thông tin của nó

    def list_courses(self):
        print("\n=== LIST OF COURSES ===")
        for c in self.__courses:
            c.list() # Đa hình: tương tự như trên

    def show_student_marks(self):
        print("\n--- Show Marks ---")
        cid = input("Enter course id to view marks: ")

        if cid in self.__marks:
            print(f"\n=== MARKS FOR COURSE ID: {cid} ===")
            for s in self.__students:
                mark = self.__marks[cid].get(s.get_id(), "N/A")
                print(f"Student: {s.get_name()} (ID: {s.get_id()}) -> Mark: {mark}")
        else:
            print("Invalid course id!")


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    app = StudentMarkManagement()

    app.add_students()
    app.add_courses()
    app.input_marks()

    app.list_courses()
    app.list_students()
    app.show_student_marks()
