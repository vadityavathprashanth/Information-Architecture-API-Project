import redis
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def search_by_field(prefix, field, value):
    keys = r.keys(f"{prefix}:*")
    for key in keys:
        record = json.loads(r.get(key))
        if record.get(field) == value:
            return record
    return None

# 1. Retrieve Computer Science department
cs_department = search_by_field("departments", "dept_name", "CompSci")
print("Department - Computer Science:")
print(json.dumps(cs_department, indent=2))

# 2. Retrieve student Peter Lynch
student_lynch = search_by_field("students", "name", "Peter Lynch")
print("\nStudent - Peter Lynch:")
print(json.dumps(student_lynch, indent=2))

# 3. Retrieve course Data Engineering
course_data_eng = search_by_field("courses", "title", "Data Engineering")
print("\nCourse - Data Engineering:")
print(json.dumps(course_data_eng, indent=2))
