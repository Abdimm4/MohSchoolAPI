from flask import Flask, jsonify, request
from database import get_connection

app = Flask(__name__)


# HOME
@app.route("/")
def home():
    return "Moh School Management API is running!"


# =========================
# STUDENTS
# =========================

@app.route("/students", methods=["GET"])
def get_students():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM Students WHERE Student_ID = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    cursor.close()
    db.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student)


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    db = get_connection()
    cursor = db.cursor()

    sql = """
        INSERT INTO Students
        (Student_ID, First_Name, Last_Name, GPA, Enrolled_Date, Expected_Grad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        data["Student_ID"],
        data["First_Name"],
        data["Last_Name"],
        data["GPA"],
        data["Enrolled_Date"],
        data["Expected_Grad"]
    )

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Student added successfully"}), 201


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    db = get_connection()
    cursor = db.cursor()

    sql = """
        UPDATE Students
        SET First_Name = %s,
            Last_Name = %s,
            GPA = %s,
            Enrolled_Date = %s,
            Expected_Grad = %s
        WHERE Student_ID = %s
    """

    values = (
        data["First_Name"],
        data["Last_Name"],
        data["GPA"],
        data["Enrolled_Date"],
        data["Expected_Grad"],
        student_id
    )

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Student updated successfully"})


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM Students WHERE Student_ID = %s",
        (student_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Student deleted successfully"})


# =========================
# TEACHERS
# =========================

@app.route("/teachers", methods=["GET"])
def get_teachers():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Teacher")
    teachers = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(teachers)


@app.route("/teachers/<int:teacher_id>", methods=["GET"])
def get_teacher(teacher_id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM Teacher WHERE Teacher_ID = %s",
        (teacher_id,)
    )

    teacher = cursor.fetchone()

    cursor.close()
    db.close()

    if teacher is None:
        return jsonify({"error": "Teacher not found"}), 404

    return jsonify(teacher)


# =========================
# FACULTY
# =========================

@app.route("/faculty", methods=["GET"])
def get_faculty():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Faculty")
    faculty = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(faculty)


@app.route("/faculty/<int:faculty_id>", methods=["GET"])
def get_faculty_member(faculty_id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM Faculty WHERE Faculty_ID = %s",
        (faculty_id,)
    )

    faculty_member = cursor.fetchone()

    cursor.close()
    db.close()

    if faculty_member is None:
        return jsonify({"error": "Faculty member not found"}), 404

    return jsonify(faculty_member)


# =========================
# COURSES
# =========================

@app.route("/courses", methods=["GET"])
def get_courses():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(courses)


@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM Courses WHERE Course_ID = %s",
        (course_id,)
    )

    course = cursor.fetchone()

    cursor.close()
    db.close()

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(course)


# =========================
# CLASSES / ENROLLMENTS
# =========================

@app.route("/classes", methods=["GET"])
def get_classes():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            cl.Class_ID,
            s.First_Name,
            s.Last_Name,
            c.Course_Name,
            c.Course_Code,
            cl.Grade
        FROM Classes cl
        JOIN Students s
            ON cl.Student_ID = s.Student_ID
        JOIN Courses c
            ON cl.Course_ID = c.Course_ID
    """)

    classes = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(classes)


@app.route("/classes/<int:class_id>", methods=["GET"])
def get_class(class_id):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            cl.Class_ID,
            s.First_Name,
            s.Last_Name,
            c.Course_Name,
            c.Course_Code,
            cl.Grade
        FROM Classes cl
        JOIN Students s
            ON cl.Student_ID = s.Student_ID
        JOIN Courses c
            ON cl.Course_ID = c.Course_ID
        WHERE cl.Class_ID = %s
    """, (class_id,))

    class_data = cursor.fetchone()

    cursor.close()
    db.close()

    if class_data is None:
        return jsonify({"error": "Class not found"}), 404

    return jsonify(class_data)


# =========================
# RUN API
# =========================

if __name__ == "__main__":
    app.run()