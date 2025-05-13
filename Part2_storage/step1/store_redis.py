import redis
import json
import os

# Load data from previously saved JSON files
def load_json_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Connect to Redis (adjust host/port if needed)
r = redis.Redis(host='localhost', port=6379, db=0)

# Load datasets
departments = load_json_data('../departments.json')
students = load_json_data('../students.json')
courses = load_json_data('../courses.json')

# Store Departments
for i, dept in enumerate(departments):
    key = f"departments:{i+1}"
    r.set(key, json.dumps(dept))

# Store Students
for i, student in enumerate(students):
    key = f"students:{i+1}"
    r.set(key, json.dumps(student))

# Store Courses
for i, course in enumerate(courses):
    key = f"courses:{i+1}"
    r.set(key, json.dumps(course))

print(" All data successfully stored in Redis!")



