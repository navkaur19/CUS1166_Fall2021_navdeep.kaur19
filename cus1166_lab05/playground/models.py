from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__= "courses"

    id = db.Column(db.Integer,primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    #Relationship fields
    registeredStudents = db.relationship("RegisteredStudent", backref="courses", lazy=True)

    def add_registeredstudent(self, name, grade):
        new_registeredstudent = RegisteredStudent(name=name, grade=grade, course_id=self.id)
        db.session.add(new_registeredstudent)
        db.session.commit()


class RegisteredStudent(db.Model):
    __tablename__= "registeredstudent"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.String, nullable = False)

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
