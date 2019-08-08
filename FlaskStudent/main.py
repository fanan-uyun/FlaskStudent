# import os
import pymysql
from flask import Flask
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect # 导入csrf校验模块,csrfProtect在1.0之后移除

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 关联csrf和flask应用
csrf = CSRFProtect(app)
# 使用类配置加载
app.config.from_object('config.DebugConfig')


# 关联sqlalchemy和flask应用
db = SQLAlchemy(app)


# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# # app.config返回类字典对象，里面用来存放当前app实例的配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR,"Student.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config.from_pyfile('settings.py')

