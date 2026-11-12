
from flask import Flask, render_template, request, redirect, url_for
from database import connect_db, create_table

app = Flask(__name__)

create_table()


@app.route("/")
def home():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"].strip()
    age = request.form["age"]
    course = request.form["course"].strip()

    if not name or not course:
        return redirect(url_for("home"))

    try:
        age = int(age)

        if age <= 0:
            return redirect(url_for("home"))

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )

        connection.commit()
        connection.close()

    except ValueError:
        return redirect(url_for("home"))

    return redirect(url_for("home"))
@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword", "").strip()

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ("%" + keyword + "%",)
    )

    students = cursor.fetchall()
    connection.close()

    return render_template("index.html", students=students)
@app.route("/update/<int:student_id>", methods=["POST"])
def update(student_id):
    name = request.form["name"].strip()
    age = request.form["age"]
    course = request.form["course"].strip()

    try:
        age = int(age)

        if not name or not course or age <= 0:
            return redirect(url_for("home"))

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE students SET name=?, age=?, course=? WHERE student_id=?",
            (name, age, course, student_id)
        )

        connection.commit()
        connection.close()

    except ValueError:
        return redirect(url_for("home"))

    return redirect(url_for("home"))
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)
