<h1 align="center"> 🎓 University Management System API</h1>


This is a Flask-based REST API project for accessing university departments, students, and courses data from a PostgreSQL database.  
It provides easy-to-use endpoints, Swagger API documentation, and a modern web interface for testing.

---

## 🚀 Features

- RESTful API GET endpoints for:
  - **Departments** with instructor details
  - **Students** with course enrollment details
  - **Courses** with instructor teaching details
- **Swagger API Documentation** (`Flasgger` powered)
- **PostgreSQL database** integration
- **Responsive Web Interface** (HTML/CSS)
- Modular code structure using Flask **Blueprints**
- Pagination support for all APIs
- **CORS** support enabled for cross-origin access

---

## 📦 Prerequisites

- Python 3.x
- PostgreSQL database (with university data loaded)
- `pip` package manager

---

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database connection:**
   - Update your **`db.py`** file with correct PostgreSQL credentials (host, port, username, password, database name).

---

## 🗂 Project Structure

```plaintext
.
├── app.py               # Main Flask app
├── db.py                # PostgreSQL connection setup
├── requirements.txt     # Python dependencies
├── routes/              # API route handlers
│   ├── departments.py
│   ├── students.py
│   └── courses.py
└── webpage/             # Static web portal
    └── index.html
```

---

## ▶️ Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the endpoints:**
   - Web Portal: [http://127.0.0.1:5000](http://127.0.0.1:5000)
   - Swagger API Documentation: [http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

---

## 🔥 Web Interface

The web interface provides:

- **University Portal Theme** 🎓
- Quick links to:
  - Departments API
  - Students API
  - Courses API
- Embedded Swagger API documentation

---

## 🖼 Screenshots

### 1. Main University Portal
![Main Portal](screenshots/main-portal.png)

---

### 2. Departments API Response
![Departments API](screenshots/departments-api.png)

---

### 3. Students API Response
![Students API](screenshots/students-api.png)

---

### 4. Courses API Response
![Courses API](screenshots/courses-api.png)

---

### 5. Swagger API Documentation Interface
![Swagger Interface](screenshots/swagger-1.png)

![Swagger Courses](screenshots/swagger-courses.png)

![Swagger Departments](screenshots/swagger-departments.png)

![Swagger Students](screenshots/swagger-students.png)

## 📚 API Endpoints

All APIs support **pagination** via:

- `page` (default = 1)
- `page_size` (default = 10)

Common JSON response structure:

```json
{
  "code": 1,
  "msg": "Success",
  "data": {
    "records": [],
    "total": 0
  }
}
```

---

### 🧬 Departments

- **Endpoint:** `/departments`
- **Returns:** List of departments and associated instructors.

---

### 🧑‍🏫 Students

- **Endpoint:** `/students`
- **Returns:** List of students and enrolled courses.

---

### 📚 Courses

- **Endpoint:** `/courses`
- **Returns:** List of courses and teaching instructors.

---

## ⚙️ Dependencies

- **Flask** - Web framework
- **Flasgger** - Swagger API Documentation
- **Flask-RESTX** - API abstraction layer (optional)
- **Flask-CORS** - Cross-Origin Resource Sharing
- **psycopg2** - PostgreSQL Adapter for Python

---

## 🧪 API Testing Scenarios (Swagger Testing)

| Test No. | Input (Page, Page Size)            | Expected Behavior                                   | Status     |
|----------|------------------------------------|----------------------------------------------------|------------|
| 1        | Page = 1, Page Size = 1             | Successfully fetch 1 record                         | ✅ Passed  |

<img src="screenshots/testing-1.png" alt="Test 1" width="100%" />

| Test No. | Input (Page, Page Size)            | Expected Behavior                                   | Status     |
|----------|------------------------------------|----------------------------------------------------|------------|
| 2        | Page = 1, Page Size = 0             | Error: "Enter a valid page size greater than 0"     | ✅ Passed  |

<img src="screenshots/testing-2.png" alt="Test 2" width="100%" />

| Test No. | Input (Page, Page Size)            | Expected Behavior                                   | Status     |
|----------|------------------------------------|----------------------------------------------------|------------|
| 3        | Page = 1, Page Size = (empty)       | Defaults to page_size = 10                          | ✅ Passed  |

<img src="screenshots/testing-3.png" alt="Test 3" width="100%" />

| Test No. | Input (Page, Page Size)            | Expected Behavior                                   | Status     |
|----------|------------------------------------|----------------------------------------------------|------------|
| 4        | Page = (empty), Page Size = (empty) | Defaults to page = 1, page_size = 10                | ✅ Passed  |

<img src="screenshots/testing-4.png" alt="Test 4" width="100%" />

| Test No. | Input (Page, Page Size)            | Expected Behavior                                   | Status     |
|----------|------------------------------------|----------------------------------------------------|------------|
| 5        | Page = 0, Page Size = (empty)       | Error: "Enter a valid page number greater than 0"   | ✅ Passed  |

<img src="screenshots/testing-5.png" alt="Test 5" width="100%" />


## 👨‍💻 Developed by

<p align="center"><b><span style="font-size:2em;">Prashanth Vadityavath</span></b></p>

---


