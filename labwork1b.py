def input_number_of_students():
    return int(input("Enter number of students in the class: "))

def input_students(n):
    students = []
    print(f"\n--- Entering information for {n} student(s) ---")
    for i in range(n):
        print(f"Student {i+1}:")
        sid = input("  id: ")
        
        name = input("  name: ")
        dob = input("  DoB (dd/mm/yyyy): ")
        student = {"id": sid, "name": name, "dob": dob}
        students.append(student)
    return students

def input_number_of_courses():
    return int(input("\nEnter number of courses: "))

def input_courses(m):
    courses = []
    marks = {}
    print(f"\n--- Entering information for {m} course(s) ---")
    for i in range(m):
        print(f"Course {i+1}:")
        cid = input("  id_course: ")
        name = input("  name: ")
        course = {"id_course": cid, "name": name}
        courses.append(course)
        marks[cid] = {}
    return courses, marks

def input_marks(students, courses, marks):
    print("\n--- Input Marks ---")
    while True:
        cid = input("Enter course id for mark: ")
        course_exists = False
        for c in courses:
            if c["id_course"] == cid:
                course_exists = True
                break
                
        if course_exists:
            print(f"Entering marks for course ID: {cid}")
            for student in students:
                student_id = student["id"]
                student_name = student["name"]
                mark = float(input(f"  Mark for {student_name} (ID: {student_id}): "))
                marks[cid][student_id] = mark
            break
        else:
            print("Invalid course id! Please try again.")


#-----2.LISTING FUNCTION-------------
def list_courses(courses):
    print("\n=== LIST OF COURSES ===")
    for c in courses:
        print(f"ID: {c['id_course']} | Name: {c['name']}")

def list_students(students):
    print("\n=== LIST OF STUDENTS ===")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks(students, courses, marks):
    print("\n--- Show Marks ---")
    while True:
        cid = input("Enter course id to view marks: ")
        
        if cid in marks:
            print(f"\n=== MARKS FOR COURSE ID: {cid} ===")
            for s in students:
                # Lấy điểm, nếu chưa nhập thì trả về "N/A"
                m = marks[cid].get(s['id'], "N/A")
                print(f"Student: {s['name']} (ID: {s['id']}) -> Mark: {m}")
            break # Exit the loop after successfully showing marks
        else:
            print("Invalid course id! Please try again.")


# --- 3.MAIN PROGRAM------

if _name_ == "_main_":
    # Nhập thông tin sinh viên
    num_students = input_number_of_students()
    student_list = input_students(num_students)

    # Nhập thông tin môn học
    num_courses = input_number_of_courses()
    course_list, marks_dict = input_courses(num_courses)

    # Nhập điểm
    input_marks(student_list, course_list, marks_dict)

    # Hiển thị dữ liệu theo yêu cầu đề bài
    list_courses(course_list)
    list_students(student_list)
    show_student_marks(student_list, course_list, marks_dict)
