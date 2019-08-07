"""
项目管理文件
"""

from FlaskStudent.models import db
from FlaskStudent.views import app

if __name__ == "__main__":
    db.create_all()
    app.run()