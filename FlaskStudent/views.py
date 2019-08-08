"""
视图和路由文件
"""
import hashlib
from flask import request
from flask import redirect

from flask import render_template
from FlaskStudent.main import app
from FlaskStudent.models import *
from FlaskStudent.main import session

def SetPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method == 'POST':
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        identity = form_data.get("identity")

        user = User()
        user.username = username
        user.password = SetPassword(password)
        user.identity = int(identity)
        user.save()

        return redirect('/login/')
    return render_template("register.html")

@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            db_password = user.password
            md5_password = SetPassword(password)
            if md5_password == db_password:
                # 验证成功，跳转首页
                response = redirect('/index/')
                # 设置cookie
                response.set_cookie("username",username)
                response.set_cookie("user_id",str(user.id))
                # 设置session
                session["username"] = username
                # 返回跳转页面
                return response
    return render_template("login.html")

@app.route("/index/")
def index():
    print(session.get('username'))
    return render_template("index.html")

@app.route("/logout/",methods=["GET","POST"])
def logout():
    response = redirect('/login/')
    for key in request.cookies:
        response.delete_cookie(key)
    del session["username"]
    return response


@app.route("/student_list/")
def student_list():
    students = Student.query.all()
    return render_template("student_lists.html",**locals())



