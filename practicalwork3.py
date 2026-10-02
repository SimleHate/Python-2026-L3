#Practical_work_3
import math
import numpy as np


class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def input(self):
        self.__id = input("  Student ID: ")
        self.__name = input("  Student Name: ")
        self.__dob = input("  DoB (dd/mm/yyyy): ")

    def list(self):
        print(f"ID: {self.__id:<10} | Name: {self.__name:<20} | DoB: {self.__dob:<12} | GPA: {self.__gpa:.1f}")


class Course:
    def __init__(self, cid="", name="", credits=0):
        self.__id = cid
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def input(self):
        self.__id = input("  Course ID: ")
        self.__name = input("  Course Name: ")
        self.__credits = int(input("  Credits: "))

    def list(self):
        print(f"ID: {self.__id:<10} | Name: {self.__name:<20} | Credits: {self.__credits}")


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # Cấu trúc: { course_id: { student_id: mark } }

    def add_students(self):
        n = int(input("Enter number of students in the class: "))
        print(f"\n--- Entering information for {n} student(s) ---")
        for i in range(n):
            print(f"Student {i+1}:")
            s = Student()
            s.input()
            self.__students.append(s)

    def add_courses(self):
        n = int(input("\nEnter number of courses: "))
        print(f"\n--- Entering information for {n} course(s) ---")
        for i in range(n):
            print(f"Course {i+1}:")
            c = Course()
            c.input()
            self.__courses.append(c)
            self.__marks[c.get_id()] = {}

    def input_marks(self):
        print("\n--- Input Marks ---")
        cid = input("Enter course id for mark: ")

        course = next((c for c in self.__courses if c.get_id() == cid), None)

        if course:
            print(f"Entering marks for course: {course.get_name()}")
            for s in self.__students:
                val = float(input(f"  Mark for {s.get_name()} (ID: {s.get_id()}): "))
                
                # 1. Dùng math.floor() làm tròn xuống 1 chữ số thập phân khi nhập
                floored_mark = math.floor(val * 10) / 10.0
                self.__marks[cid][s.get_id()] = floored_mark

            # Tự động tính lại GPA và sắp xếp lại danh sách sinh viên
            self.calculate_gpas()
            self.sort_students_by_gpa()
        else:
            print("Invalid course id!")

    def calculate_gpas(self):
        """2. Tính GPA trọng số theo số tín chỉ sử dụng numpy.array"""
        if not self.__courses or not self.__students:
            return

        for student in self.__students:
            sid = student.get_id()
            marks_list = []
            credits_list = []

            for course in self.__courses:
                cid = course.get_id()
                if cid in self.__marks and sid in self.__marks[cid]:
                    marks_list.append(self.__marks[cid][sid])
                    credits_list.append(course.get_credits())

            if credits_list:
                # Tạo numpy array
                np_marks = np.array(marks_list)
                np_credits = np.array(credits_list)

                # Phép tính trọng số: sum(mark * credit) / sum(credits)
                total_credits = np.sum(np_credits)
                if total_credits > 0:
                    weighted_gpa = np.sum(np_marks * np_credits) / total_credits
                    # Làm tròn xuống 1 chữ số thập phân bằng math.floor
                    student.set_gpa(math.floor(weighted_gpa * 10) / 10.0)

    def sort_students_by_gpa(self):
        """3. Sắp xếp sinh viên theo GPA giảm dần sử dụng numpy.argsort"""
        if not self.__students:
            return

        # Tạo mảng numpy chứa điểm GPA của tất cả sinh viên
        gpas = np.array([s.get_gpa() for s in self.__students])

        # argsort sắp xếp tăng dần -> đảo ngược [::-1] để thành giảm dần
        sorted_indices = np.argsort(gpas)[::-1]

        # Cập nhật danh sách sinh viên theo thứ tự mới
        self.__students = [self.__students[i] for i in sorted_indices]

    def list_students(self):
        print("\n=== LIST OF STUDENTS (SORTED BY GPA DESCENDING) ===")
        if not self.__students:
            print("No students found.")
            return
        for s in self.__students:
            s.list()

    def list_courses(self):
        print("\n=== LIST OF COURSES ===")
        if not self.__courses:
            print("No courses found.")
            return
        for c in self.__courses:
            c.list()

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

    def run(self):
        """Vòng lặp Menu giao diện dòng lệnh (CLI)"""
        while True:
            print("\n================ MENU ================")
            print("1. Input Students")
            print("2. Input Courses (with Credits)")
            print("3. Input Marks for Course")
            print("4. List Courses")
            print("5. List Students (Sorted by GPA Descending)")
            print("6. Show Course Marks")
            print("0. Exit")
            print("======================================")

            choice = input("Select an option: ").strip()

            if choice == "1":
                self.add_students()
            elif choice == "2":
                self.add_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.show_student_marks()
            elif choice == "0":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()
