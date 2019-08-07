"""
视图和路由文件
"""
from flask import render_template
from FlaskStudent.main import app
from FlaskStudent.models import Student

@app.route("/register/")
def register():
    return render_template("register.html",**locals())

@app.route("/login/")
def login():
    students = Student.query.all()
    return render_template("student_lists.html",**locals())

@app.route("/index/")
def index():
    students = Student.query.all()
    return render_template("student_lists.html",**locals())

@app.route("/logout/")
def logout():
    students = Student.query.all()
    return render_template("student_lists.html",**locals())


@app.route("/student_list/")
def student_list():
    students = Student.query.all()
    return render_template("student_lists.html",**locals())



