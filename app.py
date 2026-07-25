import os

from flask import Flask, render_template, request, redirect
import pymysql
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

connection = pymysql.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),
    database=os.environ.get("DB_NAME", "project_dashboard"),
    cursorclass=pymysql.cursors.DictCursor,
)


@app.route("/")
def home():

    search = request.args.get("search", "")
    status = request.args.get("status", "All")

    cursor = connection.cursor()

    query = "SELECT * FROM projects WHERE 1=1"
    values = []

    if search:
        query += " AND project_name LIKE %s"
        values.append("%" + search + "%")

    if status != "All":
        query += " AND status=%s"
        values.append(status)

    query += " ORDER BY id DESC"

    cursor.execute(query, tuple(values))
    projects = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) AS total FROM projects")
    total = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS completed FROM projects WHERE status='Completed'"
    )
    completed = cursor.fetchone()["completed"]

    cursor.execute(
        "SELECT COUNT(*) AS progress FROM projects WHERE status='In Progress'"
    )
    in_progress = cursor.fetchone()["progress"]

    cursor.execute(
        "SELECT COUNT(*) AS pending FROM projects WHERE status='Pending'"
    )
    pending = cursor.fetchone()["pending"]

    return render_template(
        "index.html",
        projects=projects,
        total=total,
        completed=completed,
        in_progress=in_progress,
        pending=pending,
        search=search,
        status=status,
        active="dashboard",
    )


@app.route("/add")
def add_page():
    return render_template("add.html", active="add")


@app.route("/save", methods=["POST"])
def save():

    project_name = request.form["project_name"]
    team_leader = request.form["team_leader"]
    team_members = request.form["team_members"]
    start_date = request.form["start_date"]
    deadline = request.form["deadline"]
    priority = request.form["priority"]
    progress = request.form["progress"]
    status = request.form["status"]

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO projects
        (project_name, team_leader, team_members,
        start_date, deadline,
        priority, progress, status)

        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            project_name,
            team_leader,
            team_members,
            start_date,
            deadline,
            priority,
            progress,
            status,
        ),
    )

    connection.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM projects WHERE id=%s",
        (id,),
    )

    connection.commit()

    return redirect("/")


@app.route("/edit/<int:id>")
def edit_page(id):

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM projects WHERE id=%s",
        (id,),
    )

    project = cursor.fetchone()

    return render_template(
        "edit.html",
        project=project,
        active="dashboard",
    )


@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    project_name = request.form["project_name"]
    team_leader = request.form["team_leader"]
    team_members = request.form["team_members"]
    start_date = request.form["start_date"]
    deadline = request.form["deadline"]
    priority = request.form["priority"]
    progress = request.form["progress"]
    status = request.form["status"]

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE projects

        SET

        project_name=%s,
        team_leader=%s,
        team_members=%s,
        start_date=%s,
        deadline=%s,
        priority=%s,
        progress=%s,
        status=%s

        WHERE id=%s
        """,
        (
            project_name,
            team_leader,
            team_members,
            start_date,
            deadline,
            priority,
            progress,
            status,
            id,
        ),
    )

    connection.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
