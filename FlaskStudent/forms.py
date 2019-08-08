import wtforms # 定义字段
from flask_wtf import Form # 定义表单
from wtforms import validators # 定义校验


class TeacherForm(Form):
    name = wtforms.StringField(
        label="教师姓名",
        render_kw={
            "class": "form-control",
            "placeholder": "教师姓名"
        },
        validators=[
            validators.DataRequired("姓名不可以为空")
        ]
    )
    age = wtforms.IntegerField(
        label="教师年龄",
        render_kw={
            "class": "form-control",
            "placeholder": "教师年龄"
        },
        validators=[
            validators.DataRequired("年龄不可以为空")
        ]
    )
    gender = wtforms.StringField(
        label="教师性别",
        render_kw={
            "class": "form-control",
            "placeholder": "教师性别"
        },
        validators=[
            validators.DataRequired("性别不可以为空")
        ]
    )
    course = wtforms.SelectField(
        label="学科",
        render_kw={
            "class": "form-control",
        },
        choices=[
            ("1","python"),
            ("2","java"),
            ("3","php"),
            ("4","web"),
            ("5","linux")
        ]
    )
    submit = wtforms.SubmitField(
        label="提交",
        render_kw={
            "class": "btn btn-primary btn-block",
        },
    )