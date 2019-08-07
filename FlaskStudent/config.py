import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 通用配置
class BaseConfig():
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# 调试配置
class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "Student_test.sqlite")

# 上线配置
class OnlineConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "Student.sqlite")