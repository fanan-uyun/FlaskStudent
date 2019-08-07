# import os
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# # app.config返回类字典对象，里面用来存放当前app实例的配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR,"Student.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config.from_pyfile('settings.py')
app.config.from_object('config.DebugConfig')


# 关联sqlalchemy和flask应用
db = SQLAlchemy(app)