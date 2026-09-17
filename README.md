# MohSchoolAPI

A RESTful API and web dashboard for managing school records — students, teachers, faculty, courses, and class enrollments — built with Flask and MySQL, deployed on Railway.

**Live URL:** https://mohschoolapi-production.up.railway.app/

---

## What it does

MohSchoolAPI exposes CRUD (Create, Read, Update, Delete) endpoints for a school's core records, backed by a relational MySQL database. It also includes a styled web dashboard that lets you browse all records visually instead of reading raw JSON.

## Database structure

The database (`railway` on the live deployment, `MohSchoolAPI` locally) contains five related tables:

| Table      | Description                                              |
|------------|-----------------------------------------------------------|
| `students` | Student records — name, GPA, enrollment and graduation dates |
| `teachers` | Teacher records                                            |
| `faculty`  | Faculty/staff records                                       |
| `courses`  | Course catalog — course name and code                       |
| `classes`  | Enrollment table linking students to courses, with grades (foreign keys to `students` and `courses`) |

## Technologies used

- **Backend:** Python, Flask
- **Database:** MySQL (`mysql-connector-python`)
- **Deployment:** Railway (Gunicorn WSGI server)
- **Config management:** `python-dotenv` (local environment variables)
- **Frontend:** HTML/CSS/JavaScript dashboard (vanilla JS, `fetch` API, no framework)

## API endpoints

| Method | Endpoint                  | Description                          |
|--------|----------------------------|---------------------------------------|
| GET    | `/`                        | Web dashboard (styled table browser) |
| GET    | `/students`                | List all students                    |
| GET    | `/students/<id>`           | Get a single student                 |
| POST   | `/students`                | Add a new student                    |
| PUT    | `/students/<id>`           | Update a student                     |
| DELETE | `/students/<id>`           | Delete a student                     |
| GET    | `/teachers`                | List all teachers                    |
| GET    | `/teachers/<id>`           | Get a single teacher                 |
| GET    | `/faculty`                 | List all faculty                     |
| GET    | `/faculty/<id>`            | Get a single faculty member          |
| GET    | `/courses`                 | List all courses                     |
| GET    | `/courses/<id>`            | Get a single course                  |
| GET    | `/classes`                 | List all class enrollments (joined with student and course names) |
| GET    | `/classes/<id>`            | Get a single class enrollment        |

## Example requests

**GET `/students`**
```json
[
  {
    "Student_ID": 1,
    "First_Name": "Jane",
    "Last_Name": "Doe",
    "GPA": 3.8,
    "Enrolled_Date": "2024-09-01",
    "Expected_Grad": "2028-05-15"
  }
]
```

**POST `/students`**
```json
{
  "Student_ID": 42,
  "First_Name": "Alex",
  "Last_Name": "Kim",
  "GPA": 3.6,
  "Enrolled_Date": "2026-01-15",
  "Expected_Grad": "2030-05-01"
}
```
Response:
```json
{ "message": "Student added successfully" }
```

**GET `/classes`**
```json
[
  {
    "Class_ID": 1,
    "First_Name": "Jane",
    "Last_Name": "Doe",
    "Course_Name": "Intro to Databases",
    "Course_Code": "CS210",
    "Grade": "A"
  }
]
```

## Running it locally

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root with your local MySQL credentials:
   ```
   MYSQLHOST=localhost
   MYSQLPORT=3306
   MYSQLUSER=root
   MYSQLPASSWORD=your_password
   MYSQLDATABASE=MohSchoolAPI
   ```

3. Make sure your local MySQL server has a database with the `students`, `teachers`, `faculty`, `courses`, and `classes` tables set up.

4. Run the app:
   ```bash
   python app.py
   ```

5. Visit `http://127.0.0.1:5000/` for the dashboard, or hit any endpoint directly (e.g. `http://127.0.0.1:5000/students`).

## Deployment notes

- Deployed on **Railway**, with a separate MySQL service provisioned alongside the Flask app.
- Environment variables (`MYSQLHOST`, `MYSQLPORT`, `MYSQLUSER`, `MYSQLPASSWORD`, `MYSQLDATABASE`) are configured directly in Railway's service settings.
- Table names are lowercase to match MySQL's case-sensitive table naming on Railway's Linux-based environment.