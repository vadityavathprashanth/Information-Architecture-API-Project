from pymongo import MongoClient, errors
import json
import sys

def load_json(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Failed to parse JSON in file: {file_path}")
        sys.exit(1)

def connect_to_mongodb(uri="mongodb://localhost:27017/"):
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        client.server_info()  # Trigger exception if cannot connect
        return client
    except errors.ServerSelectionTimeoutError as err:
        print("Could not connect to MongoDB:", err)
        sys.exit(1)

def insert_data(db, collection_name, data):
    try:
        if db[collection_name].count_documents({}) > 0:
            print(f"Collection '{collection_name}' already exists. Dropping and replacing...")
            db[collection_name].drop()
        db[collection_name].insert_many(data)
        print(f"Inserted {len(data)} records into '{collection_name}' collection.")
    except Exception as e:
        print(f"Error inserting data into {collection_name}:", e)

if __name__ == "__main__":
    # Connect to MongoDB
    client = connect_to_mongodb()
    db = client["university_db"]

    # Load JSON data
    departments = load_json("../departments.json")
    students = load_json("../students.json")
    courses = load_json("../courses.json")

    # Insert into MongoDB collections
    insert_data(db, "departments", departments)
    insert_data(db, "students", students)
    insert_data(db, "courses", courses)

    print("MongoDB storage complete.")
