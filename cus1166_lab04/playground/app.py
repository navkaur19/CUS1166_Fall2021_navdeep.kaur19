from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    welcome = (student_name == "Navdeep Kaur")
    return render_template("welcome.html", student_name=student_name)

class_roster = [("John", "B", "Junior"), ("Lilly", "A", "Senior"), ("Kevin", "B", "Sophomore"), ("Johnny", "C", "Freshman"),("Kayla", "B+", "Junior"), ("Navdeep", "B+", "Junior"), ("Jayden", "A", "Senior")]
@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html",class_roster = class_roster, grade_view = grade_view )
