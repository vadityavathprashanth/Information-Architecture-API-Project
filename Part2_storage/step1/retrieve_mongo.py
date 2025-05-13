from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["university_db"]

# 1. DEPARTMENTS: Total count + instructors in Computer Science
dept_count = db.departments.count_documents({})
cs_dept = db.departments.find_one({"dept_name": "Computer Science"})
cs_instructor_count = len(cs_dept['instructors']) if cs_dept else 0

print(f"Total Departments: {dept_count}")
print(f"Instructors in Computer Science: {cs_instructor_count}")

# 2. STUDENTS: Total count + courses Peter Lynch took in Fall 2023
student_count = db.students.count_documents({})
lynch_doc = db.students.find_one({"name": "Peter Lynch"})
lynch_fall_courses = 0

if lynch_doc:
    lynch_fall_courses = sum(1 for c in lynch_doc.get("courses", []) if c.get("semester") == "Fall" and c.get("year") == 2023)

print(f"\nTotal Students: {student_count}")
print(f"Courses Peter Lynch took in Fall 2023: {lynch_fall_courses}")

# 3. COURSES: Total count + instructor info for "Hands-on data science"
course_count = db.courses.count_documents({})
hands_on_doc = db.courses.find_one({"title": "Hands-on data science"})

print(f"\nTotal Courses: {course_count}")
if hands_on_doc:
    print(f"Instructors for 'Hands-on data science':")
    for inst in hands_on_doc.get("instructors", []):
        print(f"- {inst['name']} (Section: {inst['section']}, Semester: {inst['semester']}, Year: {inst['year']})")
else:
    print("Course 'Hands-on data science' not found.")
