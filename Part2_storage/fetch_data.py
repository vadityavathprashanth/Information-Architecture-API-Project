import requests

# Base URL of your running Flask API
BASE_URL = "http://127.0.0.1:5000"

# Helper function to fetch all paginated records
def fetch_all_records(endpoint):
    all_records = []
    page = 1
    while True:
        response = requests.get(f"{BASE_URL}/{endpoint}?page={page}")
        data = response.json()
        records = data['data']['records']
        if not records:
            break
        all_records.extend(records)
        page += 1
    return all_records

# Fetch from each API
departments_data = fetch_all_records("departments")
students_data = fetch_all_records("students")
courses_data = fetch_all_records("courses")

# Display counts
print(f"✅ Departments fetched: {len(departments_data)}")
print(f"✅ Students fetched: {len(students_data)}")
print(f"✅ Courses fetched: {len(courses_data)}")

# Save to local files 
import json
with open("departments.json", "w") as f:
    json.dump(departments_data, f, indent=2)

with open("students.json", "w") as f:
    json.dump(students_data, f, indent=2)

with open("courses.json", "w") as f:
    json.dump(courses_data, f, indent=2)
