from flask import Flask, send_from_directory
from flasgger import Swagger
from flask_cors import CORS  # <-- ADD THIS
from flask_restx import Api
from routes.departments import departments_bp
from routes.students import students_bp
from routes.courses import courses_bp

app = Flask(__name__)
CORS(app)  # <-- ADD THIS LINE (allow CORS for all routes)

# --- Swagger Template ---
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "University Information System API",
        "description": "API documentation for accessing University Departments, Students, and Courses information.<br><br>Developed by <b><i><span style='font-size:20px;'>Prashanth Vadityavath</span></i></b>."
    },
    "host": "127.0.0.1:5000",
    "basePath": "/",
    "schemes": ["http"],
}

swagger = Swagger(app, template=swagger_template)

# Register blueprints
app.register_blueprint(departments_bp)
app.register_blueprint(students_bp)
app.register_blueprint(courses_bp)

# Static homepage
@app.route('/')
def homepage():
    return send_from_directory('webpage', 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
